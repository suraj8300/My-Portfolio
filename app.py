from flask import Flask, render_template, request, send_from_directory
import pickle
import numpy as np
import Project1
import Project2

app = Flask(__name__)



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
        result = Project1.caesar(text, shift, choice)
    return render_template("project1/index1.html", result=result)

@app.route('/Project2')
def Project2():
    # Load the model when needed
    model = Project2.load_model()
    # You can now use the model for predictions or other tasks
    # Serve the index2.html file from the static folder
    return send_from_directory("templates/project2/", "index2_0.html")

@app.route('/predict', methods=['POST'])
def predict():
    # Load the model when needed
    model = Project2.load_model()
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