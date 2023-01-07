import mlflow
import pandas as pd
from src.models import model


def test_train_model():
    # Load the data
    df = pd.read_csv("data/processed/transfusion.csv")
    X = df.drop("target", axis=1)
    y = df["target"]

    # Train the model
    model.train_model(X, y)

    # Assert that the model was trained
    assert mlflow.active_run()


def test_evaluate_model():
    # Load the data
    df = pd.read_csv("data/processed/transfusion.csv")
    X = df.drop("target", axis=1)
    y = df["target"]

    # Train the model
    model.train_model(X, y)

    # Load the model from MLFlow
    model_uri = mlflow.get_artifact_uri("model")
    mlflow_model = mlflow.sklearn.load_model(model_uri)

    # Evaluate the model
    model.evaluate_model(mlflow_model, X, y)
