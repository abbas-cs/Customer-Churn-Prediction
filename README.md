# Customer Churn Prediction

A machine learning project to predict customer churn in retail business.

## Features

- Machine learning model for churn prediction
- FastAPI backend API
- Streamlit web interface
- Docker support

## Quick Start

1. Clone the repository
```bash
git clone https://github.com/abbas-cs/Customer-Churn-Prediction.git
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the API
```bash
uvicorn app:app --reload
```

4. Run the Streamlit UI
```bash
cd Retail_Churn_UI_streamlit
streamlit run retail_churn_ui.py
```

## Docker

Build and run using Docker:
```bash
docker build -t retail-churn .
docker run -p 8000:8000 retail-churn
```

## Project Structure

- `app.py`: FastAPI application
- `model/`: Contains ML model and prediction logic
- `Retail_Churn_UI_streamlit/`: Streamlit web interface
- `schema/`: Data validation schemas