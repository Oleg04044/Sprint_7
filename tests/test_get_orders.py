import requests
import allure

class TestGetOrders:

    def test_get_orders_returns_list(self):
        with allure.step("Получаем список заказов"):
            response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders')
        with allure.step("Проверяем, что ключ 'orders' есть и это список"):
            assert "orders" in response.json(), "Ответ не содержит ключ orders"
            assert isinstance(response.json()["orders"], list), "Orders не является списком"
