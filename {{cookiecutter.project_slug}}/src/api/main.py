import mlflow
import mlflow.sklearn
from fastapi import FastAPI
from src.models import predict

app = FastAPI()


@app.get("/predict")
def predict_handler(features: list):
    with mlflow.start_run():
        model_uri = mlflow.get_artifact_uri("model")
        model = predict.load_model(model_uri)
        return {"prediction": predict.predict(model, [features])[0]}
