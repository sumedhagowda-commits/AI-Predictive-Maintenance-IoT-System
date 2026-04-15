import streamlit as st
import pandas as pd
import joblib
import numpy as np

from src.data_loader import load_data
from src.preprocess import add_rul, preprocess

st.set_page_config(page_title="Predictive Maintenance AI", layout="wide")

st.title("🏭 AI Predictive Maintenance System")

# -----------------------------
# LOAD DATA
# -----------------------------
df = load_data("data/train_FD001.txt")
df = add_rul(df)

X, y = preprocess(df)

# -----------------------------
# LOAD MODEL + FEATURES
# -----------------------------
model = joblib.load("models/model.pkl")
feature_names = joblib.load("models/features.pkl")

st.subheader("Dataset Preview")
st.dataframe(df.head())

# -----------------------------
# AUTO SAMPLE INPUT (FIX)
# -----------------------------
sample_input = X.iloc[0:1]  # take real dataset row

# IMPORTANT: ensure correct column order
sample_input = pd.DataFrame(sample_input, columns=feature_names)

# -----------------------------
# PREDICTION
# -----------------------------
prediction = model.predict(sample_input)
prob = model.predict_proba(sample_input)[0][1]

st.subheader("Prediction Result")

if prediction[0] == 1:
    st.error("⚠ Machine Failure Expected")
else:
    st.success("✅ Machine Healthy")

st.metric("Failure Probability", f"{prob:.2f}")

# -----------------------------
# OPTIONAL VIEW
# -----------------------------
st.subheader("Sensor Snapshot Used for Prediction")
st.dataframe(sample_input)