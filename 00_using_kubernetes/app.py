import numpy as np
import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

# Predict using the model
@app.route('/predict', methods=['POST'])
def predict():
    # Load the model
    model_path = 'model/rental_prediction_model.pkl'
    model = pickle.load(open(model_path, 'rb'))

    user_input = request.json
        
    rooms = int(user_input.get('rooms',0))
    area = int(user_input.get('area',0))

    user_input_preprocessed = np.array([[rooms, area]])

    # Make a prediction
    prediction = model.predict(user_input_preprocessed)
    output = {"Rental Prediction using Built Model V3": float(prediction[0])}

    return output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)