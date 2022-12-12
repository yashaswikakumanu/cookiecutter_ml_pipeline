import pandas as pd


def get_data(path):
    df = pd.read_csv(path)
    return df


def store_data(data, path):
    data.to_csv(path, index=False)
