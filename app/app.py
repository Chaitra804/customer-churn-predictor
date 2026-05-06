import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
import sys
import os

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.predict import predict

# Page config
st.set_page_config(
    page_title="SaaS Churn Predictor",
    layout="wide"
)

# Title
st.title("📊 SaaS Customer Churn Predictor")
st.markdown("Predict whether a customer is likely to churn based on usage behavior.")

st.divider()

# Layout: 2 columns
col1, col2 = st.columns(2)

# -------- INPUT SECTION --------
with col1:
    st.subheader("🧾 Customer Details")

    usage = st.slider("Daily Usage (minutes)", 0, 200, 50)

    login = st.selectbox(
        "Login Frequency",
        ["Daily", "Weekly", "Monthly"]
    )

    ticket = st.text_area(
        "Support Ticket Message",
        placeholder="Describe customer issue (if any)..."
    )

# -------- INFO SECTION --------
with col2:
    st.subheader("📌 Input Summary")

    st.write(f"**Usage:** {usage} mins")
    st.write(f"**Login Frequency:** {login}")
    st.write(f"**Ticket Length:** {len(ticket)} characters")

# Mapping
mapping = {'Daily': 3, 'Weekly': 2, 'Monthly': 1}
login_val = mapping[login]

st.divider()

# -------- PREDICTION BUTTON --------
if st.button("🔍 Predict Churn", use_container_width=True):

    data = {
        "Account_Age_Days": 200,
        "Login_Frequency": login_val,
        "Daily_Usage_Mins": usage,
        "ticket_length": len(ticket),
        "engagement_score": usage * login_val,
        "has_complaint": int(
            any(word in ticket.lower() for word in ["issue", "error", "problem", "not working"])
        )
    }

    pred, prob = predict(data)

    st.divider()

    # -------- RESULTS --------
    st.subheader("📈 Prediction Result")

    # KPI style layout
    k1, k2 = st.columns(2)

    with k1:
        st.metric("Churn Probability", f"{prob:.2f}")

    with k2:
        if pred == 1:
            st.metric("Risk Level", "High 🔴")
        else:
            st.metric("Risk Level", "Low 🟢")

    # Progress bar
    st.progress(int(prob * 100))

    # Message
    if pred == 1:
        st.error("⚠️ Customer is likely to churn. Immediate action recommended.")
    else:
        st.success("✅ Customer is likely to stay.")

    # -------- INSIGHT SECTION --------
    st.subheader("🧠 Insights")

    if usage < 20:
        st.warning("Low usage detected → strong churn indicator")

    if login == "Monthly":
        st.warning("Low login frequency → disengagement risk")

    if len(ticket) > 50:
        st.warning("Long support message → possible dissatisfaction")

    if "issue" in ticket.lower():
        st.warning("Complaint detected in ticket")
