# app.py
from flask import Flask, request, jsonify
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__, static_folder="static")

# Load the trained model
with open("heart_disease_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def index():
    return app.send_static_file("MinorProject.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    
    # Convert input to the format expected by the model
    input_data = pd.DataFrame({
        'age': [float(data['age'])],
        'sex': [float(data['sex'])],
        'cp': [float(data['cp'])],
        'trestbps': [float(data['trestbps'])],
        'chol': [float(data['chol'])],
        'fbs': [float(data['fbs'])],
        'restecg': [float(data['restecg'])],
        'thalach': [float(data['thalach'])],
        'exang': [float(data['exang'])],
        'oldpeak': [float(data['oldpeak'])],
        'slope': [float(data['slope'])],
        'ca': [float(data['ca'])],
        'thal': [float(data['thal'])]
    })
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    
    # Get feature importance for explanation
    explanation = []
    if prediction == 1:
        feature_importance = list(zip(input_data.columns, model.feature_importances_))
        sorted_importance = sorted(feature_importance, key=lambda x: x[1], reverse=True)
        explanation = [f"{feat} contributed {imp:.2f} to this prediction" for feat, imp in sorted_importance[:3]]
        
    return jsonify({
        "prediction": "likely" if prediction == 1 else "unlikely",
        "explanation": explanation
    })

if __name__ == "__main__":
    app.run(host='localhost', port=3000, debug=True)
