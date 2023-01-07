import os
import tempfile

import pytest
import requests_mock
from src.data import ingest


@pytest.fixture
def temp_dir():
    with tempfile.TemporaryDirectory() as temp_dir:
        yield temp_dir


def test_download_file(temp_dir):
    # Mock the response from the server
    with requests_mock.Mock() as mock:
        mock.get("https://example.com/my_data.csv", text="fake,data")

        # Set the file path
        file_path = os.path.join(temp_dir, "my_data.csv")

        # Download the file
        ingest.download_file("https://example.com/my_data.csv", file_path)

        # Check that the file was downloaded
        with open(file_path, "r") as f:
            assert f.read() == "fake,data"
