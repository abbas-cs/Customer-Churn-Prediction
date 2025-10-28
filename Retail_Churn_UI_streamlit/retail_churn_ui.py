import streamlit as st
import requests


RETAIL_CHURN_URL = 'http://51.21.170.85:8000/predict'

st.title('Retail Churn Prediction')

gender = st.selectbox('Gender', ['Male', 'Female'])
SeniorCitizen = st.selectbox('Senior Citizen', ['0', '1'])
Partner = st.selectbox('Partner', ['Yes', 'No'])
Dependents = st.selectbox('Dependents', ['Yes', 'No'])
tenure = st.number_input('Tenure')
PhoneService = st.selectbox('Phone Service', ['No', 'Yes'])
MultipleLines = st.selectbox('Multiple Lines', ['No phone service', 'No', 'Yes'])
InternetService = st.selectbox('Internet Service', ['DSL', 'Fiber optic', 'No'])
OnlineSecuirty = st.selectbox('Online Security', ['No', 'Yes', 'No internet service'])
OnlineBackup = st.selectbox('Online Backup', ['Yes', 'No', 'No internet service'])
DeviceProtection = st.selectbox('Device Protection', ['No', 'Yes', 'No internet service'])
TechSupport = st.selectbox('Tech Support', ['No', 'Yes', 'No internet service'])
StreamingTV = st.selectbox('Streaming TV', ['No', 'Yes', 'No internet service'])
StreamingMovies = st.selectbox('Streaming Movies', ['No', 'Yes', 'No internet service'])
Contract = st.selectbox('Contract', ['Month-to-month', 'One year', 'Two year'])
PaperlessBilling = st.selectbox('Paperless Billing', ['Yes', 'No'])
PaymentMethod = st.selectbox('Payment Method', ['Electronic check', 'Mailed check', 'Bank transfer (automatic)',
       'Credit card (automatic)'])
MonthlyCharges = st.number_input('Monthly Charges')
TotalCharges = st.number_input('Total Charges')

if st.button('Predict', type='primary'):
    input_data = {
        'gender': gender,
        'SeniorCitizen': SeniorCitizen,
        'Partner': Partner,
        'Dependents': Dependents,
        'tenure': tenure,
        'PhoneService': PhoneService,
        'MultipleLines': MultipleLines,
        'InternetService': InternetService,
        'OnlineSecurity': OnlineSecuirty,
        'OnlineBackup': OnlineBackup,
        'DeviceProtection': DeviceProtection,
        'TechSupport': TechSupport,
        'StreamingTV': StreamingTV,
        'StreamingMovies': StreamingMovies,
        'Contract': Contract,
        'PaperlessBilling': PaperlessBilling,
        'PaymentMethod': PaymentMethod,
        'MonthlyCharges': MonthlyCharges,
        'TotalCharges': TotalCharges
    }

    try:

        response = requests.post(RETAIL_CHURN_URL, json=input_data)
        if response.status_code==200:
            result = response.json()
            if result['Prediction']==0:
                st.write('# :green[**Not Churn**]')
            elif result['Prediction']==1:
                st.write('# :red[**Churn**]')
        else:
            st.success(f'API Error {response.status_code} - {response.text}')
    
    except requests.exceptions.ConnectionError:
        st.error('Could not connect to the server')