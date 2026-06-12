# 🏦 Loan Approval Prediction – Machine Learning Project

## 📌 Project Overview
This project is a Machine Learning web application that predicts whether a loan application will be approved or rejected based on applicant financial and personal information.

The model is trained on structured banking data and deployed using Streamlit for an interactive user interface.

---

## 🎯 Objective
To build a classification model that helps predict loan approval status using features like income, credit score, loan amount, and assets.

---

## 📊 Dataset Features

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

**Target Variable:**
- Loan Status (Approved / Rejected)

---

## ⚙️ Tech Stack

- Python
- Pandas
- Scikit-learn
- Machine Learning (Random Forest Classifier)
- Streamlit
- Joblib

---

## 🧠 Machine Learning Pipeline

- Data Cleaning
- Encoding categorical variables using Pipeline
- Train-Test Split
- Model Training using Random Forest Classifier
- Evaluation using Accuracy & Confusion Matrix
- Model saved using Joblib

---

## 📈 Model Performance

- Accuracy: ~97%
- Low false approval rate (important for banking use case)
- Evaluated using confusion matrix and classification report

---

## 🚀 How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/your-username/loan-approval-prediction.git
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Streamlit app
```bash
streamlit run app.py
```

---


---

## 💡 Key Learnings

- End-to-end ML pipeline creation  
- Data preprocessing without leakage  
- Model deployment using Streamlit  
- Real-world classification problem handling  

---

## Author
Krishma Adhikari
