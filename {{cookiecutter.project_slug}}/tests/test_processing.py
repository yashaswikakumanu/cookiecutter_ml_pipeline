import os
import tempfile

import pandas as pd
import pytest
from src.data import processing


@pytest.fixture
def temp_dir():
    with tempfile.TemporaryDirectory() as temp_dir:
        yield temp_dir


def test_process_data(temp_dir):
    # Set the input and output file paths
    input_path = os.path.join(temp_dir, "input.csv")
    output_path = os.path.join(temp_dir, "output.csv")

    # Create the input file
    with open(input_path, "w") as f:
        f.write("a,b\n1,2\n3,4\n")

    # Process the data
    processing.process_data(input_path, output_path)

    # Check that the output file was created
    assert os.path.exists(output_path)

    # Check that the output data is correct
    df = pd.read_csv(output_path)
    assert df.equals(pd.DataFrame([[1, 2], [3, 4]], columns=["a", "b"]))
