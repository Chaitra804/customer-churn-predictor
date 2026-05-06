import sys
import os
import streamlit as st
import plotly.graph_objects as go
import time

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.predict import predict

# Page config
st.set_page_config(page_title="Churn AI Dashboard", layout="wide")

# ------------------ 🎬 ANIMATED UI (Framer-like feel) ------------------ #
st.markdown("""
<style>

/* 🌑 Background */
.stApp {
    background: radial-gradient(circle at top, #0A0A0A, #000000);
    color: #EDEDED;
    font-family: 'Segoe UI', sans-serif;
    animation: fadeIn 1s ease-in;
}

/* ✨ Global fade-in */
@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}

/* 🪟 Glass Card with animation */
.card {
    background: rgba(255, 77, 141, 0.05);
    border: 1px solid rgba(192,192,192,0.2);
    padding: 20px;
    border-radius: 16px;
    backdrop-filter: blur(12px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.6);
    transition: all 0.4s ease;
    animation: slideUp 0.8s ease;
}

/* Slide-up animation */
@keyframes slideUp {
    from {
        transform: translateY(20px);
        opacity: 0;
    }
    to {
        transform: translateY(0px);
        opacity: 1;
    }
}

/* Hover glow (Framer-like interaction feel) */
.card:hover {
    transform: translateY(-5px) scale(1.01);
    border: 1px solid rgba(212,175,55,0.4);
    box-shadow: 0 0 25px rgba(255,77,141,0.2);
}

/* 🪙 Title glow */
h1 {
    text-align: center;
    color: #D4AF37;
    text-shadow: 0 0 20px rgba(212,175,55,0.3);
    animation: fadeIn 1.2s ease;
}

/* 🔘 Animated Button */
.stButton>button {
    background: linear-gradient(90deg, #FF4D8D, #D4AF37);
    color: black;
    font-weight: 700;
    border-radius: 10px;
    height: 3em;
    border: none;
    transition: all 0.3s ease;
    animation: pulse 2s infinite;
}

/* Pulse animation (CTA feel) */
@keyframes pulse {
    0% {box-shadow: 0 0 0px rgba(255,77,141,0.4);}
    50% {box-shadow: 0 0 15px rgba(255,77,141,0.6);}
    100% {box-shadow: 0 0 0px rgba(255,77,141,0.4);}
}

.stButton>button:hover {
    transform: scale(1.05);
}

/* 📊 Metrics glow */
[data-testid="metric-container"] {
    background: rgba(212, 175, 55, 0.08);
    border-left: 4px solid #D4AF37;
    padding: 12px;
    border-radius: 12px;
    animation: fadeIn 1s ease;
}

</style>
""", unsafe_allow_html=True)

# ------------------ TITLE ------------------ #
st.title("📊 SaaS Customer Churn AI Dashboard")
st.markdown("<p style='text-align:center; color:#999;'>Animated AI-powered churn prediction system</p>", unsafe_allow_html=True)

st.divider()

# ------------------ INPUT ------------------ #
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("🧾 Customer Details")

    usage = st.slider("Daily Usage (minutes)", 0, 200, 80)
    login = st.selectbox("Login Frequency", ["Daily", "Weekly", "Monthly"])
    ticket = st.text_area("Support Ticket")

    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📌 Live Input Summary")

    st.markdown(f"🔹 Usage: **{usage} mins**")
    st.markdown(f"🔹 Login: **{login}**")
    st.markdown(f"🔹 Ticket Length: **{len(ticket)}** chars")

    st.markdown('</div>', unsafe_allow_html=True)

mapping = {'Daily': 3, 'Weekly': 2, 'Monthly': 1}
login_val = mapping[login]

st.divider()

# ------------------ PREDICTION ------------------ #
if st.button("⚡ Run AI Prediction", use_container_width=True):

    with st.spinner("Analyzing customer behavior..."):
        time.sleep(1.2)  # fake animation delay

    data = {
        "Account_Age_Days": 200,
        "Login_Frequency": login_val,
        "Daily_Usage_Mins": usage,
        "ticket_length": len(ticket),
        "engagement_score": usage * login_val,
        "has_complaint": int(any(w in ticket.lower() for w in ["issue","error","problem"]))
    }

    pred, prob = predict(data)

    st.divider()

    # ---------------- RESULT ---------------- #
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📈 Prediction Result")

    c1, c2 = st.columns(2)

    with c1:
        st.metric("Churn Probability", f"{prob:.2f}")

    with c2:
        st.metric("Risk Level", "HIGH 🔴" if pred else "LOW 🟢")

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prob * 100,
        title={'text': "Risk Meter"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "#FF4D8D"},
            'steps': [
                {'range': [0, 40], 'color': "#111"},
                {'range': [40, 70], 'color': "#D4AF37"},
                {'range': [70, 100], 'color': "#FF4D8D"}
            ]
        }
    ))

    st.plotly_chart(fig, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- AI EXPLANATION ---------------- #
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("🤖 Reasoning Engine")

    reasons = []

    if usage < 20:
        reasons.append("Low engagement detected (usage drop)")

    if login == "Monthly":
        reasons.append("Infrequent login pattern")

    if len(ticket) > 50:
        reasons.append("High support dependency")

    if "issue" in ticket.lower():
        reasons.append("Explicit complaint signal")

    if not reasons:
        reasons.append("Healthy customer behavior detected")

    for r in reasons:
        st.markdown(f"• {r}")

    st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- INSIGHTS ---------------- #
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📊 Behavioral Pattern")

    fig2 = go.Figure([go.Bar(
        x=["Usage", "Login Score", "Support Load"],
        y=[usage, login_val * 30, len(ticket)]
    )])

    st.plotly_chart(fig2, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)