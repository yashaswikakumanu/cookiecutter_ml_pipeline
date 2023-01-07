import mlflow
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def train_model(X, y):
    # Split the data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Create the model
    model = RandomForestClassifier()

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Calculate the accuracy
    accuracy = accuracy_score(y_test, y_pred)

    # Log the accuracy with MLFlow
    with mlflow.start_run() as run:
        mlflow.log_metric("accuracy", accuracy)
        mlflow.sklearn.log_model(model, "model")


def evaluate_model(model, X, y):
    # Make predictions
    y_pred = model.predict(X)

    # Calculate the accuracy
    accuracy = accuracy_score(y, y_pred)

    # Log the accuracy with MLFlow
    with mlflow.start_run() as run:
        mlflow.log_metric("accuracy", accuracy)
