###########################################################################################################
# All imports here

from flask import Flask, render_template, request, send_from_directory
import pickle
import numpy as np
import pandas as pd



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

# Define the relative path to your pickle file
PICKLE_FILE_PATH = "projectFiles/project2/data/Al_wire_rod.sav"  # Update with your project name
# PICKLE_FILE_PATH = "notebooks/project2/Al_wire_rod.sav"

def load_model():
    # Load the machine learning model
    with open(PICKLE_FILE_PATH, 'rb') as f:
        model = pickle.load(f)
    return model

# Load the model when needed
model = load_model()

#####################################################################################################
# Flask Application

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

#################################################################################################


#######################################################################################################
# Project 1 : Cypher encode decoder

@app.route('/Project1', methods=["GET","POST"])
def Project1():
    result = ""
    if request.method == "POST":
        text = request.form["text"].lower()
        shift = int(request.form["shift"])
        choice = request.form["choice"]
        print(f"Received: text={text}, shift={shift}, choice={choice}")
        result = caesar(text, shift, choice)
    return render_template("index1.html", result=result)

#######################################################################################################
# Project 2 : AL wire rod predictor

@app.route('/Project2')
def Project2():

    # You can now use the model for predictions or other tasks
    # Serve the index2.html file from the static folder
    return render_template('index2.html')

@app.route('/predict', methods=['POST'])
def predict():
    
    # Get form data
    casting_temp = float(request.form['casting_temp'])
    rolling_speed = float(request.form['rolling_speed'])
    cooling_rate = float(request.form['cooling_rate'])

    # Prepare data for prediction
    input_data = [[casting_temp, rolling_speed, cooling_rate]]
    input_df = pd.DataFrame(input_data, columns=["Casting_Temperature_C", "Rolling_Speed_m_min", "Cooling_Rate_C_s"])

    # Predict using the model
    prediction = model.predict(input_df) # Use the DataFrame with column names for prediction
    
    # Unpack the predictions if they are separate values in a multi-output model
    if len(prediction[0]) == 3:
        uts, elongation, conductivity = prediction[0]
    else:
        # Handle the case where the model returns a single prediction array
        uts = prediction[0][0]
        elongation = prediction[0][1] if len(prediction[0]) > 1 else None
        conductivity = prediction[0][2] if len(prediction[0]) > 2 else None

    # Manually build the response HTML to show the predictions
    result_html = f"""
    <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f5f5f5;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }}
                .container {{
                    background-color: white;
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    text-align: center;
                }}
                .result {{
                    font-size: 18px;
                    margin-bottom: 20px;
                }}
                .button {{
                    padding: 10px 20px;
                    background-color: #4CAF50;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    font-size: 16px;
                }}
                .button:hover {{
                    background-color: #45a049;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h2>Prediction Results</h2>
                <div class="result">UTS (MPa): {uts:.2f}</div>
                <div class="result">Elongation (%): {elongation:.2f}</div>
                <div class="result">Conductivity (% IACS): {conductivity:.2f}</div>
                <form action="/Project2" method="get">
                    <button class="button" type="submit">Predict for Next Rod</button>
                </form>
            </div>
        </body>
    </html>
    """

    # Return the HTML response
    return result_html

#######################################################################################################


if __name__ == '__main__':
    app.run(debug=True)

#########################################################################################################
# Git push commands

"""
git add .
git commit -m "New project added."
git push -u origin main
"""

