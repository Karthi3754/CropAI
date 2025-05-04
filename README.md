# 🌾 Crop Prediction Web App

This is a machine learning-powered web application that predicts the most suitable crop based on soil and environmental parameters like Nitrogen, Phosphorus, Potassium, Temperature, Humidity, pH, and Rainfall.

## 🚀 Features

- Frontend built with HTML, CSS, JavaScript
- Backend built using Python Flask
- Crop prediction using a trained ML model
- Instant prediction results via REST API

---

## 🧠 Tech Stack

| Frontend  | Backend     | Machine Learning     |
|-----------|-------------|----------------------|
| HTML/CSS  | Python Flask | Scikit-Learn, Joblib |
| JavaScript | Flask-CORS  | DecisionTree, RandomForest |

---

```bash
# 📁 Clone the repository or unzip the folder
git clone https://github.com/your-username/crop-prediction.git
cd CropPredictionProject

# 📂 Go to backend folder
cd backend

# 🐍 Set up Python virtual environment
python -m venv venv

# ✅ Activate the environment

# ➤ For Git Bash or WSL:
source venv/Scripts/activate

# ➤ For Windows CMD:
venv\Scripts\activate

# ➤ For PowerShell:
.\venv\Scripts\Activate.ps1

# 📦 Install required Python packages
pip install flask flask-cors joblib numpy

# (Optional) Install these if you're training your own model
pip install pandas scikit-learn

# ▶️ Run Flask server
python app.py

# ✅ Expected output:
# Model and Label Encoder loaded successfully!
# * Running on http://127.0.0.1:5000/

# 🌐 Running the Frontend

# ➤ Option 1: Manual
# Open the file: frontend/index.html in your browser

# ➤ Option 2: Live Server (VS Code)
# Right-click on frontend/index.html → "Open with Live Server"

# 🧪 Sample Input:
# 135, 82, 166, 5.3, 0.74, 0.27, 14.71, 147.87, 53.86, 47.16, 54.12

# ✅ Prediction Output Example:
# mango
```

Happy Coding ✨
