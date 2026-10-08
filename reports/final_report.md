# Final Project Report

## Goal
Predict late delivery risk before the delivery happens.

## Engineering decisions

### Validation

Temporal split was used to simulate future predictions.

### Leakage prevention

Historical seller statistics use only information available before prediction time.

### Models

Compared:

- Dummy baseline
- Logistic Regression
- Random Forest
- CatBoost

### Explainability

Implemented:

- SHAP values
- calibration analysis
- false positive / false negative analysis

### Production roadmap

- MLflow
- API serving
- monitoring
- retraining pipeline