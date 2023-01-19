from typing import Dict, List

import requests


def send_request(url: str, features: List) -> Dict:
    """
    Sends a GET request to the specified URL with the provided features in the request body as a JSON object.

    :param url: str: The URL to send the request to.
    :param features: list: A list of features to include in the request body.
    :return: dict: The JSON response from the server.
    """
    response = requests.get(url, json={"features": features})
    return response.json()
