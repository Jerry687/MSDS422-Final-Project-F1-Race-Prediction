from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

app = FastAPI(title="F1 Top-10 Prediction API")

class PredictionRequest(BaseModel):
    features: dict

class PredictionResponse(BaseModel):
    top10_probability: float
    predicted_top10: int

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictionResponse)
def predict(req: PredictionRequest):
    # TODO: load persisted model + scaler + feature list and score req.features
    # This file is a generated template from notebook.
    return PredictionResponse(top10_probability=0.5, predicted_top10=0)
