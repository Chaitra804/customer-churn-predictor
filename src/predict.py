import joblib # pyright: ignore[reportMissingImports]
import pandas as pd
import json

# Load model
model = joblib.load("models/churn_model.pkl")

# Load feature list
with open("models/features.json") as f:
    features = json.load(f)

def predict(data):
    df = pd.DataFrame([data])
    df = df[features]

    pred = model.predict(df)[0]
    prob = model.predict_proba(df)[0][1]

    return pred, prob