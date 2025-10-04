import streamlit as st
import numpy as np
import pandas as pd
import pickle

with open('Scaler.pkl','rb') as f:
    scaler = pickle.load(f)

with open('Logistic_model.pkl','rb') as file:
    model = pickle.load(file)

st.title("Diabetes Prediction")

col1, col2 = st.columns(2)

with col1:
    preg = st.number_input('Pregnancies',value=0.0)
    bp = st.number_input('BloodPressure',value=0.0)
    insulin = st.number_input('Insulin',value=0.0)
    dpf = st.number_input('DiabetesPedigreeFunction',value=0.0)

with col2:
    glucose = st.number_input('Glucose',value=0.0)
    skinthick = st.number_input('SkinThickness',value=0.0)
    bmi = st.number_input('BMI',value=0.0)
    age = st.number_input('Age',value=0.0)

input_data = pd.DataFrame([{
    "Pregnancies":preg,
    "Glucose":glucose,
    "BloodPressure": bp,
    "SkinThickness": skinthick,
    "Insulin": insulin,
    "BMI": bmi,
    "DiabetesPedigreeFunction": dpf,
    "Age": age
    }])
scaled_data = scaler.transform(input_data)

if st.button("Predict"):
    prediction = model.predict(scaled_data)
    if prediction[0] == 0:
        st.success("Patient is Non-Diabetic")
    else:
        st.success("Patient is Diabetic")
