import requests
import allure
from urls import GET_ORDERS
from data import HTTP_200_OK

class TestGetOrders:

    def test_get_orders_success(self):
        with allure.step("Получаем список заказов"):
            response = requests.get(GET_ORDERS)
        with allure.step("Проверяем код и наличие данных"):
            assert response.status_code == HTTP_200_OK
            assert "orders" in response.json()
