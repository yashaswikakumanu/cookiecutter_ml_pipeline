import pandas as pd
from src.data import preprocessing


def test_preprocessing():
    df = pd.DataFrame([[1, 2], [3, 4]], columns=["a", "b"])
    processed_df = preprocessing.preprocess(df)

    # Assert that the preprocessing was successful
    assert processed_df.equals(df)
