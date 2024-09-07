import allure
import pytest
import requests


class TestOrdersByClient:

    @allure.title("Получение заказов пользователя с авторизацией")
    def test_new_order_with_login(self, get_token):
        headers = {
            'Authorization': get_token
        }
        response = requests.get('https://stellarburgers.nomoreparties.site/api/orders',headers=headers)
        assert response.status_code == 403

    @allure.title("Получение заказов пользователя без авторизации")
    def test_orders_no_login(self):
        response = requests.get('https://stellarburgers.nomoreparties.site/api/orders')
        assert response.status_code == 401