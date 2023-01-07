import os

import requests
from src.data import processing


def download_file(url, file_path):
    # Download the file from the given URL
    response = requests.get(url)
    response.raise_for_status()

    # Save the file
    with open(file_path, "w") as f:
        f.write(response.text)


def ingest_data():
    # Set the input and output file paths
    input_path = "data/raw/transfusion.data"
    output_path = "data/processed/transfusion.csv"

    # Download the file if it doesn't already exist
    if not os.path.exists(input_path):
        download_file(
            "https://archive.ics.uci.edu/ml/machine-learning-databases/blood-transfusion/transfusion.data",
            input_path,
        )

    # Process the data
    processing.process_data(input_path, output_path)
