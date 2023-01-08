from unittest import mock

import pytest
from src.api import main, utils


@pytest.fixture
def api_url():
    return "http://localhost:8000/predict"


@pytest.fixture
def mock_server():
    with mock.patch("requests.get") as m:
        mock_store = mock.MagicMock()
        m.return_value = mock_store
        yield mock_store


def test_predict_handler(api_url, mock_server):

    mock_server.json.return_value = {"prediction": 0.8}
    # Send a request to the API
    response = utils.send_request(api_url, [1, 2, 3, 4])

    # Check that the API returned a prediction
    assert "prediction" in response
