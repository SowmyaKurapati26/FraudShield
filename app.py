# app.py

import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

# =========================
# Load trained model
# =========================
with open("models/fraud_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("💳 Credit Card Fraud Detection")
st.write("Upload a CSV file with transactions, and the model will predict fraud or not fraud.")

# =========================
# File Upload
# =========================
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("📂 Uploaded Data Preview:")
    st.dataframe(df.head())

    # =========================
    # Preprocessing
    # =========================
    if "Amount" in df.columns and "Time" in df.columns:
        scaler = StandardScaler()
        df['norm_amount'] = scaler.fit_transform(df['Amount'].values.reshape(-1,1))
        df['norm_time'] = scaler.fit_transform(df['Time'].values.reshape(-1,1))
        df = df.drop(['Time','Amount'], axis=1)
    else:
        st.error("❌ CSV must contain 'Time' and 'Amount' columns.")
        st.stop()

    # Ensure "Class" column is not used in prediction (if present)
    if "Class" in df.columns:
        df_features = df.drop("Class", axis=1)
    else:
        df_features = df

    # =========================
    # Prediction
    # =========================
    predictions = model.predict(df_features)
    df["Prediction"] = predictions
    df["Prediction_Label"] = df["Prediction"].map({0: "✅ Not Fraud", 1: "⚠️ Fraud"})

    # =========================
    # Results
    # =========================
    st.subheader("🔎 Predictions")
    st.dataframe(df[["Prediction_Label"]].head(20))  # show first 20 predictions

    fraud_count = (df["Prediction"] == 1).sum()
    not_fraud_count = (df["Prediction"] == 0).sum()

    st.write(f"✅ Not Fraud: {not_fraud_count}")
    st.write(f"⚠️ Fraud: {fraud_count}")

    # =========================
    # Download Results
    # =========================
    csv_out = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="⬇️ Download Predictions as CSV",
        data=csv_out,
        file_name="fraud_predictions.csv",
        mime="text/csv"
    )
