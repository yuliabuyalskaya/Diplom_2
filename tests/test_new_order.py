
import allure
import json
import pytest
import requests


class TestNewOrder:
    @allure.title("Создание заказа с авторизацией без ингредиентов")
    def test_new_order_with_login(self, get_token):
        headers = {
            'Authorization': get_token
        }
        payload = {
            "ingredients": []
        }
        response = requests.post('https://stellarburgers.nomoreparties.site/api/orders', json=payload, headers=headers)
        assert response.status_code == 403

    @allure.title("Создание заказа без авторизации без ингредиентов")
    def test_new_order_no_login(self):
        payload = {
            "ingredients": []
        }
        response = requests.post('https://stellarburgers.nomoreparties.site/api/orders', json=payload)
        assert response.status_code == 400

    @allure.title("Создание заказа с авторизацией с ингредиентами")
    def test_new_order_with_login_with_ingredients(self, get_token):
        headers = {
            'Authorization': get_token
        }
        data = {
            "ingredients": ["60d3b41abdacab0026a733c6","609646e4dc916e00276b2870"]
        }
        response = requests.post('https://stellarburgers.nomoreparties.site/api/orders', headers = headers, json = data)
        assert response.status_code == 403

    @allure.title("Создание заказа с авторизацией без ингредиентов")
    def test_new_order_with_login_no_ingredients(self,get_token):
        headers = {
            'Authorization': get_token
        }
        data = {
            "ingredients": []
        }
        response = requests.post('https://stellarburgers.nomoreparties.site/api/orders', headers=headers, json=data)
        assert response.status_code == 403

    @allure.title("Создание заказа с авторизацией с неправильным ингредиентом")
    def test_new_order_with_login_invalid_ingredients(self, get_token):
        headers = {
            'Authorization': get_token
        }
        data = {
            "ingredients": ["invalid"]
        }
        response = requests.post('https://stellarburgers.nomoreparties.site/api/orders', headers=headers, json=data)
        assert response.status_code == 403







