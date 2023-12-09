from flask import Flask, request, jsonify
import numpy as np
from http import HTTPStatus
import pickle
import pandas as pd

app = Flask(__name__)

# Load the pre-trained model
with open('./pkls/best_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route("/")
def _health_check():
    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": {},
    }
    return response

@app.route('/predict', methods=['POST'])
def predict_price():
    try:
        data = request.get_json()

        # Create a DataFrame from the input data
        input_data = pd.DataFrame(data, index=[0])

        # Make prediction
        prediction = model.predict(input_data.values)

        # Return the result
        return jsonify({'predicted_price': float(prediction[0])})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(port=5000)