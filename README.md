# 🏦 Loan Approval Prediction – End-to-End Machine Learning Project

## 📌 Overview
This project is an end-to-end Machine Learning web application that predicts whether a loan application will be **approved or rejected** based on applicant financial and personal information.

The goal is to help financial institutions assess loan risk using data-driven decisions.

The model is deployed using **Streamlit**, providing an interactive interface for real-time predictions.

---

## 🎯 Problem Statement
Banks receive many loan applications daily. Manually evaluating each application is time-consuming and error-prone.

This project automates the process by predicting loan approval using machine learning.

---

## 📊 Dataset Features

### Input Features:
- Number of Dependents  
- Education  
- Self Employed  
- Annual Income  
- Loan Amount  
- Loan Term  
- CIBIL Score  
- Residential Assets Value  
- Commercial Assets Value  
- Luxury Assets Value  
- Bank Asset Value  

### Target Variable:
- Loan Status (Approved / Rejected)

---

## ⚙️ Tech Stack

- Python 🐍  
- Pandas & NumPy  
- Scikit-learn  
- Machine Learning (Random Forest Classifier)  
- Streamlit (Web App)  
- Joblib (Model Serialization)

---

## 🧠 Machine Learning Pipeline

- Data Cleaning (removed irrelevant columns like ID)
- Feature Engineering & preprocessing
- Encoding categorical variables using Pipeline
- Train-Test Split with stratification
- Model Training using Random Forest Classifier
- Model Evaluation using Accuracy & Confusion Matrix
- Saved model using Joblib for deployment

---

## 📈 Model Performance

- Accuracy: **~97%**
- Very low false approval rate (important for banking risk control)
- Evaluated using:
  - Confusion Matrix
  - Classification Report

---

## 🚀 How to Run Locally

### 1. Clone Repository
```bash
git clone https://github.com/Krishma-adhikari/loan-approval-prediction.git
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Streamlit App
```bash
streamlit run app.py
```


---

## 🏗️ Project Workflow

```
Data Collection → Data Cleaning → Feature Engineering → Model Training → Evaluation → Deployment (Streamlit)
```

---

## 💡 Key Learnings

- Built a complete ML pipeline from scratch  
- Understood importance of avoiding data leakage  
- Implemented production-style preprocessing using Pipeline  
- Deployed ML model using Streamlit  
- Handled real-world classification problem  

---

## 📌 Business Impact

- Reduces manual loan approval workload  
- Helps identify risky loan applicants  
- Improves decision-making efficiency in banking systems  

---

## 👨‍💻 Author

**Krishma Adhikari**

---
