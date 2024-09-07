import pytest
import requests
from helpers import  generating_cred
import allure



@pytest.fixture
def get_token():
    payload = generating_cred()
    response = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', json=payload)
    assert response.status_code == 200, "Failed to register and get token"
    token = response.json()['accessToken']
    return f"Bearer {token}"


@pytest.fixture
def get_refresh_token():
    response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/login",data={"email": "budjrvoiak@yandex.ru", "password": "wwqmqsimoi"})
    return response.json()['refreshToken']




