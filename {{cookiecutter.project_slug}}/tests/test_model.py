from unittest import mock

import mlflow
import pandas as pd
import pytest
from mlflow import MlflowClient
from src.models import model

"""
Recency (months),Frequency (times),Monetary (c.c. blood),Time (months),"target"
2,50,12500,98,1
0,13,3250,28,1
1,24,6000,77,0
4,4,1000,4,0
"""


def get_latest_run():
    client = MlflowClient()
    return client.get_run(client.search_runs(["0"])[0].info.run_id)


@pytest.fixture
def mock_read_csv():
    with mock.patch("pandas.read_csv") as m:
        mock_store = mock.MagicMock()
        mock_store.return_value = pd.DataFrame(
            {
                "col1": [1, 2, 3, 4, 5, 6],
                "col2": [1, 2, 3, 4, 5, 6],
                "target": [1, 1, 1, 0, 0, 0],
            }
        )
        m.return_value = mock_store.return_value
        yield m


def test_mock_read_csv(mock_read_csv):
    df = pd.read_csv("data/processed/transfusion.csv")
    assert df.equals(
        pd.DataFrame(
            {
                "col1": [1, 2, 3, 4, 5, 6],
                "col2": [1, 2, 3, 4, 5, 6],
                "target": [1, 1, 1, 0, 0, 0],
            }
        )
    )


@pytest.mark.skip(reason="BUG:mlflow.active_run should give run info but returns None")
def test_train_model(mock_read_csv):
    # Load the data
    df = pd.read_csv("data/processed/transfusion.csv")
    X = df.drop("target", axis=1)
    y = df["target"]

    # Train the model
    model.train_model(X, y)

    # Assert that the model was trained
    assert mlflow.active_run()


# @pytest.mark.skip(reason="don't have data csv file")
def test_evaluate_model(mock_read_csv):
    # Load the data
    df = pd.read_csv("data/processed/transfusion.csv")
    X = df.drop("target", axis=1)
    y = df["target"]

    # Train the model
    model.train_model(X, y)

    # Get the current run
    # run = mlflow.active_run()
    run = get_latest_run()

    model_uri = run.info.artifact_uri

    # Load the model from MLFlow
    # model_uri = mlflow.get_artifact_uri(artifact_path="model")
    print(model_uri)
    mlflow_model = mlflow.sklearn.load_model(f"{model_uri}/model")

    # Evaluate the model
    model.evaluate_model(mlflow_model, X, y)
