from catboost import CatBoostClassifier


def train_catboost(X_train, y_train, X_valid, y_valid):
    model = CatBoostClassifier(
        iterations=500,
        learning_rate=0.03,
        depth=6,
        eval_metric="AUC",
        auto_class_weights="Balanced",
        random_seed=42,
        early_stopping_rounds=50,
    )

    model.fit(
        X_train,
        y_train,
        eval_set=(X_valid, y_valid),
    )

    return model


if __name__ == "__main__":
    print("Training entrypoint")