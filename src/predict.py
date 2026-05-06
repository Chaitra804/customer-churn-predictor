import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def predict(data):

    usage = data["Daily_Usage_Mins"]
    login = data["Login_Frequency"]
    ticket_len = data["ticket_length"]
    complaint = data["has_complaint"]

    # Feature engineering
    low_usage = 1 if usage < 30 else 0
    low_login = 1 if login == 1 else 0
    inactivity_risk = 1 if usage < 15 else 0
    complaint_score = ticket_len / 50 if complaint else 0

    # Weighted risk model (core improvement)
    risk_score = (
        0.35 * low_usage +
        0.25 * low_login +
        0.20 * complaint_score +
        0.20 * inactivity_risk
    )

    # Convert to probability
    prob = sigmoid(risk_score * 2.5)

    # Prediction threshold
    pred = 1 if prob > 0.5 else 0

    return pred, prob