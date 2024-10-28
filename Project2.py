from flask import Flask, render_template, request, send_from_directory
import pickle
import numpy as np
import Project1
import Project2


# Define the relative path to your pickle file
# PICKLE_FILE_PATH = "projectFiles/project2/data/Al_wire_rod.sav"  # Update with your project name
PICKLE_FILE_PATH = "notebooks/project2/Al_wire_rod.sav"


def load_model():
    # Load the machine learning model
    with open(PICKLE_FILE_PATH, 'rb') as f:
        model = pickle.load(f)
    return model