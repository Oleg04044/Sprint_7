import requests
import allure
import pytest

class TestCreateOrder:

    @pytest.mark.parametrize("colors", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    def test_create_order_with_various_colors(self, colors):
        payload = {
            "firstName": "Test",
            "lastName": "Courier",
            "address": "Test street",
            "metroStation": 4,
            "phone": "+79999999999",
            "rentTime": 2,
            "deliveryDate": "2025-06-23",
            "comment": "test comment",
            "color": colors
        }
        with allure.step(f"Создаём заказ с цветами: {colors}"):
            response = requests.post(
                'https://qa-scooter.praktikum-services.ru/api/v1/orders',
                json=payload
            )
        with allure.step("Проверяем создание заказа"):
            assert response.status_code == 201, f"Неверный статус при создании заказа {colors}"
            assert "track" in response.json(), "Ответ не содержит track"
