import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Ensure ml_model directory exists before saving the model
os.makedirs("backend/ml_model", exist_ok=True)

def train_model(csv_path):
    # Load dataset
    df_train = pd.read_csv(csv_path, nrows=500)

    # Identify label column (Assuming last column is the label)
    label_col = df_train.columns[-1]

    # Encode target labels (Crop names to numbers)
    label_encoder = LabelEncoder()
    df_train[label_col] = label_encoder.fit_transform(df_train[label_col])

    # Split data into features and target
    X_train = df_train.drop(columns=[label_col])
    y_train = df_train[label_col]

    # Train Random Forest model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save trained model and label encoder inside backend/ml_model/
    joblib.dump(model, "backend/ml_model/crop_model.pkl")
    joblib.dump(label_encoder, "backend/ml_model/label_encoder.pkl")

    print("✅ Model training completed! `crop_model.pkl` and `label_encoder.pkl` saved.")

# Run training
if __name__ == "__main__":
    train_model("dataset/dataset.csv")  # Update path if needed
