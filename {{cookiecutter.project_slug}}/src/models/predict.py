import mlflow.sklearn


def predict(model, X):
    return model.predict(X)


def load_model(model_path):
    return mlflow.sklearn.load_model(model_path)
