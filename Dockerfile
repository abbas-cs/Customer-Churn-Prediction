# use python 3.11 base Image
FROM python:3.11-slim

# set working directory
WORKDIR /app

# copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy rest of application code
COPY . .

# Expose the application port
EXPOSE 8000

# Command to start fast-api application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]