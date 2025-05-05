# Import Libraries
import numpy as np
import pickle
from flask import Flask, request

import numpy as np
import logging
import os
import boto3
import shutil

# Load the model from S3 to local path
model_path = "model/model.pkl"

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the prediction
@app.route('/', methods=['GET'])
def index():
    return "Welcome to the Rental Price Prediction API!"

# Define a route for the prediction
@app.route('/predict', methods=['POST'])
def predict():
    
    # Load the model from the local path
    model = pickle.load(open(model_path, 'rb'))

    # Get user input from the request
    user_input = request.json

    # Extract the number of rooms and square footage from the input
    rooms = int(user_input.get('rooms', 0))
    sqft = int(user_input.get('sqft', 0))

    # Prepare the input for the model
    user_input_prediction = np.array([[rooms, sqft]])

    # Predict the rental price using the model
    predicted_rental_price = model.predict(user_input_prediction)

    # Prepare the output in a dictionary format
    output = {"Rental Price Prediction Using Model V4": float(predicted_rental_price[0])}

    # Return the output as a JSON response
    return output

# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
