import pandas as pd
from src.data import preprocessing


def process_data(input_path, output_path):
    # Load the data
    df = pd.read_csv(input_path)

    # Preprocess the data
    df = preprocessing.preprocess(df)

    # Save the processed data
    df.to_csv(output_path, index=False)
