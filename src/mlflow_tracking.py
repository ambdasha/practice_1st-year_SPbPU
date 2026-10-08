import mlflow


def log_experiment(model_name, params, metrics):
    with mlflow.start_run():
        mlflow.log_param("model", model_name)

        for key, value in params.items():
            mlflow.log_param(key, value)

        for key, value in metrics.items():
            mlflow.log_metric(key, value)