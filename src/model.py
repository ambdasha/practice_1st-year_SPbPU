from pathlib import Path
from catboost import CatBoostClassifier

MODEL_PATH = Path("models/catboost_delivery_risk.cbm")


def create_model():
    return CatBoostClassifier(
        iterations=500,
        learning_rate=0.03,
        depth=6,
        eval_metric="AUC",
        auto_class_weights="Balanced",
        random_seed=42,
        early_stopping_rounds=50,
    )


def save_model(model, path=MODEL_PATH):
    Path(path).parent.mkdir(exist_ok=True)
    model.save_model(str(path))


def load_model(path=MODEL_PATH):
    model = CatBoostClassifier()
    model.load_model(str(path))
    return model