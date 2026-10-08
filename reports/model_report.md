# Model Report

## Problem
Predict late delivery risk for e-commerce orders.

## Validation strategy

Temporal split:
- train
- validation
- future test

## Main conclusions

Feature engineering was more important than increasing model complexity.

Important signals:
- promised delivery window
- seller reliability
- geography
- logistics distance
- order timing

## Production recommendations

Deploy with monitoring:
- prediction drift
- feature drift
- precision/recall drift