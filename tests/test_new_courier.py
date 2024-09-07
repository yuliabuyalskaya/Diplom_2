import allure
import json

import pytest
import requests
from helpers import generating_cred

class TestRegistrationNewCourier:
    @allure.title("Регистрация курьера с валидными данными")
    def test_new_courier_registration_valid(self):
        payload = generating_cred()
        responce = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', data = payload)
        assert responce.status_code == 200

    @allure.title("Регистрация курьера с невалидными данными (уже зарегистрированный курьер)")
    def test_new_courier_registration_not_new_courier(self):
        payload = generating_cred()
        responce = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', data=payload)
        responce = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', data=payload)
        assert responce.status_code == 403 and 'User already exists' in responce.text

    @pytest.mark.parametrize(
        'data',
        [
             generating_cred().pop('name'),
             generating_cred().pop('password'),
             generating_cred().pop('email')
        ]
    )
    @allure.title("Регистрация курьера с с незаполненным одним из обязательных полей")
    def test_new_corier_registration_not_all_field(self,data):
        payload = data
        responce = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', data=payload)
        assert responce.status_code == 403 and 'Email, password and name are required fields' in responce.text






