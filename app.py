from fastapi import FastAPI
from schema.user_input import UserInput
import pandas as pd
from fastapi.responses import JSONResponse
from model.predict import predict, model, MODEL_VERSION

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Retail Churn API'}

@app.get('/health')
def health_check():
    return{
        'status': 'OK',
        'version': MODEL_VERSION
    }
@app.post('/predict')
def predict_churn(user_input: UserInput):

    input_df ={
        'gender': user_input.gender,
        'SeniorCitizen': user_input.SeniorCitizen,
        'Partner': user_input.Partner,
        'Dependents': user_input.Dependents,
        'tenure': user_input.tenure,
        'PhoneService': user_input.PhoneService,
        'MultipleLines': user_input.MultipleLines,
        'InternetService': user_input.InternetService,
        'OnlineSecurity': user_input.OnlineSecurity,
        'OnlineBackup': user_input.OnlineBackup,
        'DeviceProtection': user_input.DeviceProtection,
        'TechSupport': user_input.TechSupport,
        'StreamingTV': user_input.StreamingTV,
        'StreamingMovies': user_input.StreamingMovies,
        'Contract': user_input.Contract,
        'PaperlessBilling': user_input.PaperlessBilling,
        'PaymentMethod': user_input.PaymentMethod,
        'MonthlyCharges': user_input.MonthlyCharges,
        'TotalCharges': user_input.TotalCharges
    }

    try:

        predictions = predict(input_df)

        return JSONResponse(status_code=200, content={'Prediction' : predictions})
    
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))
