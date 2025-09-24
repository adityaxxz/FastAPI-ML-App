# FastAPI ML Application

A machine learning API built with FastAPI that predicts insurance premium categories based on user data using RandomForestClassifier.

## Features

- FastAPI backend with ML model integration
- Streamlit frontend for easy interaction
- Dockerized application with multi-service setup
- Health check endpoints for monitoring
- Detailed prediction responses with confidence scores

## Tech Stack

- **Backend**: FastAPI, Python 3.11
- **Frontend**: Streamlit
- **Containerization**: Docker
- **Process Management**: Supervisor
- **ML Model**: RandomForestClassifier (scikit-learn)

## Quick Start

### Running with Docker

```bash
# Pull the Docker image
docker pull adityaxxz/fastapi-ml-api:latest

# Run the container
docker run -p 8000:8000 -p 8501:8501 adityaxxz/fastapi-ml-api:latest
```

### Running Locally

1. Create and activate a virtual environment:

> I've used uv coz its rust-based and 100x faster than pip

```bash
uv venv
.venv/bin/activate
```

2. Install dependencies:

```bash
uv pip install -r requirements.txt
```

3. Start the FastAPI server:

```bash
uvicorn app:app --reload
or 
py -m uvicorn app:app --port=8000--reload
```

4. In a separate terminal, start the Streamlit frontend:

```bash
streamlit run frontend.py
```

## API Endpoints

- `GET /`: Home endpoint
- `GET /health`: Health check endpoint
- `POST /predict`: Prediction endpoint

- `Swagger UI`: http://localhost:8000/docs

### Prediction Input Schema

```json
{
  "age": 30,
  "weight": 65.0,
  "height": 1.7,
  "income_lpa": 10.0,
  "smoker": false,
  "city": "Mumbai",
  "occupation": "private_job"
}
```

### Prediction Response Schema

```json
{
  "predicted_category": "Medium",
  "confidence": 0.85,
  "class_probabilities": {
    "Low": 0.10,
    "Medium": 0.85,
    "High": 0.05
  }
}
```

## Project Structure

```
fastapi-ml/
├── app.py                 # FastAPI application
├── frontend.py            # Streamlit frontend
├── model/
│   ├── predict.py         # Prediction logic
│   └── model.pkl          # Serialized ML model
├── schema/
│   ├── user_input.py      # Input validation schema
│   └── prediction_response.py  # Response schema
├── config/
│   └── city_tier.py       # City tier configuration
├── dockerfile             # Docker configuration
└── requirements.txt       # Python dependencies
``
