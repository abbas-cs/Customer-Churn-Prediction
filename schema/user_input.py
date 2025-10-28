from pydantic import BaseModel
from typing import Literal

class UserInput(BaseModel):
    gender : Literal['Male', 'Female']
    SeniorCitizen : Literal['0', '1']
    Partner : Literal['Yes', 'No']
    Dependents : Literal['Yes', 'No']
    tenure : int
    PhoneService : Literal['Yes', 'No']
    MultipleLines : Literal['No phone service', 'No', 'Yes']
    InternetService : Literal['DSL', 'Fiber optic', 'No']
    OnlineSecurity : Literal['No', 'Yes', 'No internet service']
    OnlineBackup : Literal['Yes', 'No', 'No internet service']
    DeviceProtection : Literal['Yes', 'No', 'No internet service']
    TechSupport : Literal['No', 'Yes', 'No internet service']
    StreamingTV : Literal['No', 'Yes', 'No internet service']
    StreamingMovies : Literal['No', 'Yes', 'No internet service']
    Contract : Literal['Month-to-month', 'One year', 'Two year']
    PaperlessBilling : Literal['Yes', 'No']
    PaymentMethod : Literal['Electronic check', 'Mailed check', 'Bank transfer (automatic)',
       'Credit card (automatic)']
    MonthlyCharges: float
    TotalCharges: float
