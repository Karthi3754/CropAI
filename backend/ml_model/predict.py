import sys
import json
import joblib
import pandas as pd
import os

# Get the correct path for the model and label encoder
base_path = os.path.dirname(__file__)
model_path = os.path.join(base_path, "crop_model.pkl")
label_encoder_path = os.path.join(base_path, "label_encoder.pkl")

# Check if model files exist
if not os.path.exists(model_path):
    print("Error: 'crop_model.pkl' not found. Please train the model first.")
    sys.exit(1)

if not os.path.exists(label_encoder_path):
    print("Error: 'label_encoder.pkl' not found. Please train the model first.")
    sys.exit(1)

# Load trained model and label encoder
model = joblib.load(model_path)
label_encoder = joblib.load(label_encoder_path)

# Check if arguments are provided
if len(sys.argv) < 2:
    print("Error: No input features provided. Please pass feature values as a JSON string.")
    sys.exit(1)

try:
    # Parse input features
    input_features = json.loads(sys.argv[1])

    # Ensure input is a list or dict
    if not isinstance(input_features, (list, dict)):
        raise ValueError("Invalid input format. Must be a JSON array or object.")

    # Convert input to DataFrame
    feature_names = model.feature_names_in_
    if isinstance(input_features, dict):
        input_features = [input_features[f] for f in feature_names]  # Ensure correct order
    
    features_df = pd.DataFrame([input_features], columns=feature_names)

    # Make prediction
    prediction = model.predict(features_df)
    predicted_crop = label_encoder.inverse_transform(prediction)[0]

    print(f"Predicted Crop: {predicted_crop}")

except json.JSONDecodeError:
    print("Error: Failed to parse JSON input. Ensure it's a valid JSON string.")
    sys.exit(1)
except ValueError as ve:
    print(f"Error: {ve}")
    sys.exit(1)
except Exception as e:
    print(f"Unexpected Error: {e}")
    sys.exit(1)
