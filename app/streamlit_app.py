import streamlit as st
import joblib
import numpy as np

model = joblib.load("models/model.joblib")
scaler = joblib.load("models/scaler.joblib")

st.title("🎓 Student Performance Predictor")

st.write("Enter the input parameters below:")

hours_studied = st.slider("Hours Studied", 1, 9, 5)
previous_scores = st.slider("Previous Exam Score", 40, 100, 70)
extracurricular = st.selectbox("Participates in Extracurricular Activities?", ["Yes", "No"])
sleep_hours = st.slider("Sleep Hours", 4, 9, 7)
papers_practiced = st.slider("Sample Papers Practiced", 0, 9, 5)

extracurricular_num = 1 if extracurricular == "Yes" else 0
X_input = np.array([[hours_studied, previous_scores, extracurricular_num, sleep_hours, papers_practiced]])
X_scaled = scaler.transform(X_input)

prediction = model.predict(X_scaled)[0]

st.subheader("📈 Predicted Performance Index:")
st.success(f"{prediction:.2f}")
