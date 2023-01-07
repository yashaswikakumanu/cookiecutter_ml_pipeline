import pytest
from src.api import main, utils


@pytest.fixture
def api_url():
    return "http://localhost:8000/predict"


def test_predict_handler(api_url):
    # Send a request to the API
    response = utils.send_request(api_url, [1, 2, 3, 4])

    # Check that the API returned a prediction
    assert "prediction" in response
