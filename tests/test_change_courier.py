import pytest
import requests
from helpers import generating_cred
import allure


class TestChangeCourier:

    @pytest.mark.parametrize(
        'data',
        [
            generating_cred().pop('name'),
            generating_cred().pop('password'),
            generating_cred().pop('email')
        ]
    )
    @allure.title("Обновление данных о пользователе (с авторизацией)")
    def test_update_courier(self, get_token, data):
        headers = {
            'Authorization': get_token
        }
        update_data = data
        response = requests.patch('https://stellarburgers.nomoreparties.site/api/auth/user', json=update_data, headers=headers)
        assert response.status_code == 400

    @pytest.mark.parametrize(
        'data',
        [
            generating_cred().pop('name'),
            generating_cred().pop('password'),
            generating_cred().pop('email')
        ]
    )
    @allure.title("Обновление данных о пользователе (без авторизации)")
    def test_update_courier_invalid(self, data):
        update_data = {
            "name": "New Name",
            "email": "dgsjhgdjhsgdjgdjl@yandex.com"
        }
        response = requests.patch('https://stellarburgers.nomoreparties.site/api/auth/user', json=update_data)
        assert response.status_code == 401




