from flask import Flask, request, jsonify
import joblib
import numpy as np
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

# Load the trained model and label encoder
model_path = os.path.join(os.path.dirname(__file__), "ml_model", "crop_model.pkl")
encoder_path = os.path.join(os.path.dirname(__file__), "ml_model", "label_encoder.pkl")

try:
    model = joblib.load(model_path)
    label_encoder = joblib.load(encoder_path)
    print("Model and Label Encoder loaded successfully!")
except Exception as e:
    print(f"Error loading model or label encoder: {e}")
    model = None
    label_encoder = None

@app.route("/")
def home():
    return "Crop Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    if not model or not label_encoder:
        return jsonify({"error": "Model not loaded"}), 500

    try:
        data = request.get_json()
        features = data.get("features")

        if not features or not isinstance(features, list):
            return jsonify({"error": "Invalid input format. Expecting a list of features."}), 400

        # Convert input to numpy array and reshape
        features_array = np.array(features).reshape(1, -1)

        # Predict the crop
        prediction = model.predict(features_array)
        predicted_crop = label_encoder.inverse_transform(prediction)[0]

        return jsonify({"predicted_crop": predicted_crop})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
