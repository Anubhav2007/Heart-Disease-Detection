# Random Forest Prediction 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
file_path = r"C:\Users\KIIT\OneDrive\Desktop\code\Minor Project\heart disease dataset.csv"
df = pd.read_csv(file_path)

# Split features and target
X = df.drop(columns=["target"])
y = df["target"]

# Train-test split (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Optimized Random Forest model
rf_model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    min_samples_split=10,
    random_state=42
)
rf_model.fit(X_train, y_train)

# Evaluate model performance
y_pred = rf_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Optimized Random Forest Accuracy: {accuracy * 100:.2f}%")

import pickle
with open("heart_disease_model.pkl", "wb") as f:
    pickle.dump(rf_model, f)