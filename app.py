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
    preg = st.number_input('Pregnancies',min_value=1,max_value=12,value=1)
    bp = st.number_input('BloodPressure',min_value=0,max_value=140,value=100)
    insulin = st.slider('Insulin',min_value=0,max_value=900,value=80)
    dpf = st.slider('DiabetesPedigreeFunction',min_value=0.0,max_value=2.5,value=0.5)

with col2:
    glucose = st.slider('Glucose',min_value=0, max_value=200, value=100)
    skinthick = st.slider('SkinThickness',min_value=0, max_value=100, value=20)
    bmi = st.number_input('BMI', min_value=10.0,max_value=50.0,value=18.5)
    age = st.number_input('Age',min_value=21,max_value=80,value=21)

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
