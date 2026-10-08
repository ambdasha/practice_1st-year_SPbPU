from sklearn.metrics import (
    roc_auc_score,
    average_precision_score,
    f1_score,
)


def evaluate(y_true, probability, threshold=0.5):
    prediction = (probability >= threshold).astype(int)

    return {
        "roc_auc": roc_auc_score(y_true, probability),
        "pr_auc": average_precision_score(y_true, probability),
        "f1": f1_score(y_true, prediction),
    }