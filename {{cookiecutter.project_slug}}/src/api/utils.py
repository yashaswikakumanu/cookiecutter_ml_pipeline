import requests


def send_request(url, features):
    response = requests.get(url, json={"features": features})
    return response.json()
