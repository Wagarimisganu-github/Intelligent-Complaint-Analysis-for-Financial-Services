import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("src/model/sentiment_model.pkl")  # Adjust path if needed

# Upload CSV
st.title("Intelligent Complaint Sentiment Analyzer")
uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("📄 Uploaded Data", df)

    # Prediction (assumes there's a text column named 'complaint_what_happened')
    df['prediction'] = df['complaint_what_happened'].apply(model.predict)

    st.subheader("📊 Prediction Results")
    st.write(df[['complaint_what_happened', 'prediction']])

    # 🔹 Optional Visualization
    st.subheader("📈 Prediction Distribution")
    pred_counts = df['prediction'].value_counts()
    st.bar_chart(pred_counts)

    # Optional: Save or Download
    # df.to_csv("predicted_output.csv", index=False)
