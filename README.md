# Diabetes Prediction

A machine learning project to predict diabetes using patient health data. The project includes **data preprocessing, model training, and deployment** using Streamlit and Docker.

---

## Workflow

## Import Dependencies: 

 - import numpy as np
 - import pandas as pd
 - import matplotlib.pyplot as plt
 - import seaborn as sns
 - from sklearn.model_selection import train_test_split
 - from sklearn.preprocessing import StandardScaler
 - from sklearn.linear_model import LogisticRegression
 - from sklearn.metrics import accuracy_score, confusion_matrix

---

## 📊 Load Dataset

- **Basic Checks -**
- **Rows:** 768  
- **Source:** [Kaggle / UCI Diabetes Dataset]  
- **Features:** Multiple patient health metrics (Glucose, BMI, Age, Pregnancies, BloodPressure, DiabetesPedigreeFunction, etc.)  
- **Target:** Diabetes (0 = No, 1 = Yes)

---

## 🧹 Data Preprocessing

- Exploratory Data Analysis (EDA)  
- Handled missing values  
- Outlier detection and removal  
- Feature scaling  
- Class imbalance handling  

---

## 🧠 Model

- **Algorithm:** Logistic Regression  
- **Train Accuracy:** 76.87%  
- **Test Accuracy:** 75.32%  

---

## 💻 Streamlit App

A **real-time web app** to predict diabetes using the trained model. Users can input patient data and get predictions instantly.

**Screenshot:**  
<img width="1362" height="594" alt="app_screenshot" src="https://github.com/user-attachments/assets/61790d59-38a9-4a87-b538-21073d6739bb" />

---

## 🐳 Docker Deployment

The app is **Dockerized** for easy deployment.
Also uploaded to Docker hub.

**Run Locally with Docker:**
```bash
# Pull the Docker image
docker pull vedant93/diabetes-app

# Run the container
docker run -p 8501:8501 diabetes-app
