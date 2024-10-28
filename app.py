from flask import Flask, render_template, request, send_from_directory
import pickle
import numpy as np


app = Flask(__name__)

#############################################################################################
# Cypher Encoder Decoder

def caesar(original_text, shift_amount, choice):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cypher_text = ""
    for i in original_text:
        if i not in alphabet:
            cypher_text += i
        else:
            if choice == "encrypt":
                cypher_text += alphabet[(alphabet.index(i) + shift_amount) % 26]
            elif choice == "decrypt":
                cypher_text += alphabet[(alphabet.index(i) - shift_amount) % 26]
    return cypher_text

#######################################################################################################

# AL wire Rod Predictor

from flask import Flask, render_template, request, send_from_directory
import pickle
import numpy as np




# Define the relative path to your pickle file
# PICKLE_FILE_PATH = "projectFiles/project2/data/Al_wire_rod.sav"  # Update with your project name
PICKLE_FILE_PATH = "notebooks/project2/Al_wire_rod.sav"


def load_model():
    # Load the machine learning model
    with open(PICKLE_FILE_PATH, 'rb') as f:
        model = pickle.load(f)
    return model

#####################################################################################################

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/Project1', methods=["GET","POST"])
def Project1():
    result = ""
    if request.method == "POST":
        text = request.form["text"].lower()
        shift = int(request.form["shift"])
        choice = request.form["choice"]
        print(f"Received: text={text}, shift={shift}, choice={choice}")
        result = caesar(text, shift, choice)
    return render_template("project1/index1.html", result=result)

@app.route('/Project2')
def project2():
    # Load the model when needed
    model = load_model()
    # You can now use the model for predictions or other tasks
    # Serve the index2.html file from the static folder
    return send_from_directory("templates/project2/", "index2_0.html")

@app.route('/predict', methods=['POST'])
def predict():
    # Load the model when needed
    model = load_model()
    # You can now use the model for predictions or other tasks
    
    # Get form data
    casting_temp = float(request.form['casting_temp'])
    rolling_speed = float(request.form['rolling_speed'])
    cooling_rate = float(request.form['cooling_rate'])

    # Prepare data for prediction
    input_data = np.array([[casting_temp, rolling_speed, cooling_rate]])
    
    # Predict using the model
    prediction = model.predict(input_data)[0]
    uts = prediction[0]
    elongation = prediction[1]
    conductivity = prediction[2]

    # Return the HTML response
    
    return render_template('index2_1.html', uts=uts, elongation=elongation, conductivity=conductivity)

if __name__ == '__main__':
    app.run(debug=True)


"""
git add .
git commit -m "Updated requirements.txt with cleaned package names and versions"
git push -u origin main
"""