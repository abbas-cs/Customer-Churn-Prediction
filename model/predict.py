import joblib
import pandas as pd

model = joblib.load('model/retial_churn_model.joblib')

MODEL_VERSION = '1.0.0'

def predict(user_input: dict):

    user_input_pd = pd.DataFrame([user_input])
    prediction = model.predict(user_input_pd)[0]

    return int(prediction)