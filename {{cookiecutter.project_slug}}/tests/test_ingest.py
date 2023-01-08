import os
import tempfile
from unittest import mock

import pytest
from src.data import ingest


@pytest.fixture
def temp_dir():
    with tempfile.TemporaryDirectory() as temp_dir:
        yield temp_dir


@pytest.fixture
def mock_download():
    with mock.patch("requests.get") as m:
        mock_store = mock.MagicMock()
        m.return_value = mock_store
        yield mock_store


def test_download_file(temp_dir, mock_download):
    # Mock the response from the server
    mock_download.text = "fake,data"

    # Set the file path
    file_path = os.path.join(temp_dir, "my_data.csv")

    # Download the file
    ingest.download_file("https://example.com/my_data.csv", file_path)

    # Check that the file was downloaded
    with open(file_path, "r") as f:
        assert f.read() == "fake,data"
