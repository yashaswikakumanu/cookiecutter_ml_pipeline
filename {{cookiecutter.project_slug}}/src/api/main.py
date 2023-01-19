from typing import Dict, List

import mlflow
import mlflow.sklearn
from fastapi import FastAPI
from src.models import predict

app = FastAPI()


@app.get("/predict")
def predict_handler(features: List[float]) -> Dict[str, float]:
    """
    This endpoint takes a list of features as input and returns a prediction.

    :param features: A list of float values representing the features used for prediction.
    :type features: List[float]
    :return: A dictionary containing the prediction result.
    :rtype: Dict[str, float]
    """
    with mlflow.start_run():
        model_uri = mlflow.get_artifact_uri("model")
        model = predict.load_model(model_uri)
    return {"prediction": predict.predict(model, [features])[0]}
