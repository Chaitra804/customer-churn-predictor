import os
import pickle
from sklearn.model_selection import train_test_split # type: ignore
from sklearn.ensemble import RandomForestClassifier # pyright: ignore[reportMissingModuleSource]
from src.data_loader import load_data
from src.preprocessing import preprocess
from src.feature_engineering import create_features

def train_model():
    df = load_data("data/raw/train.csv")

    df = preprocess(df)
    df = create_features(df)

    X = df.drop('Churn', axis=1)
    y = df['Churn']

    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(class_weight='balanced')
    model.fit(X_train, y_train)

    # Save model
    os.makedirs("models", exist_ok=True)
    with open("models/churn_model.pkl", "wb") as f:
        pickle.dump(model, f)

    # Save features
    import json
    with open("models/features.json", "w") as f:
        json.dump(list(X.columns), f)

    print("Model trained and saved!")

if __name__ == "__main__":
    train_model()