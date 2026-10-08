from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Olist Delivery Risk API")


class OrderFeatures(BaseModel):
    features: dict


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(order: OrderFeatures):
    # Real deployment loads trained model and feature pipeline.
    return {
        "risk_probability": None,
        "message": "Connect trained pipeline"
    }