import streamlit as st
import pandas as pd
import joblib

model = joblib.load('loan_model.pkl')

st.title("Loan Approval Prediction")
st.write("Enter the details to predict loan approval status.")


no_of_dependents = st.number_input("Number of Dependents", 0,10,step = 1)

education = st.selectbox("Education",["Graduate","Not Graduate"])

self_employed = st.selectbox("Self Employed",["Yes","No"])

income_annum = st.number_input("Annual Income", min_value=0)

loan_amount = st.number_input("Loan Amount", min_value=0)

loan_term = st.number_input("Loan Term (months)", min_value=1)

cibil_score = st.number_input("CIBIL Score", min_value=300, max_value=900)

residential_assets_value = st.number_input("Residential Assets Value", min_value=0)

commercial_assets_value = st.number_input("Commercial Assets Value", min_value=0)

luxury_assets_value = st.number_input("Luxury Assets Value", min_value=0)

bank_asset_value = st.number_input("Bank Asset Value", min_value=0)
if st.button("Predict Loan Status"):

    input_data = pd.DataFrame({
        "no_of_dependents": [no_of_dependents],
        "education": [education],
        "self_employed": [self_employed],
        "income_annum": [income_annum],
        "loan_amount": [loan_amount],
        "loan_term": [loan_term],
        "cibil_score": [cibil_score],
        "residential_assets_value": [residential_assets_value],
        "commercial_assets_value": [commercial_assets_value],
        "luxury_assets_value": [luxury_assets_value],
        "bank_asset_value": [bank_asset_value]
    })

    st.write("Input Preview:")
    st.dataframe(input_data)

    prediction = model.predict(input_data)[0]

    st.write("Raw prediction:", prediction)

# normalize prediction
    if isinstance(prediction, str):
     prediction = prediction.strip().lower()

    if prediction in [1, "approved", "yes", "true", "1"]:
     st.success("Loan Approved")
    else:
     st.error("Loan Rejected")