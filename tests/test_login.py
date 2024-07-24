import pytest
import requests
from helpers import generating_cred
import allure

class TestLoginCourier:
    @allure.title("Авторизация курьера с валидными данными")
    def test_login_valid(self):
        payload = {'email': 'budjrvoiak@yandex.ru', 'password': 'wwqmqsimoi'}
        responce = requests.post('https://stellarburgers.nomoreparties.site/api/auth/login', data = payload)
        assert responce.status_code == 401

    @allure.title("Авторизация курьера, который не зарегистрирован")
    def test_new_courier_registration_not_new_courier(self):
        payload = generating_cred().pop('name')
        responce = requests.post('https://stellarburgers.nomoreparties.site/api/auth/login', data=payload)
        assert responce.status_code == 401 and 'email or password are incorrect' in responce.text
