import pandas as pd
from src.model import load_model

model = load_model()


def predict_delivery_risk(features: pd.DataFrame):
    probability = model.predict_proba(features)[:, 1]
    return probability