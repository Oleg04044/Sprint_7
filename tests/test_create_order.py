import requests
import allure
import pytest
from urls import CREATE_ORDER
from data import HTTP_201_CREATED

class TestCreateOrder:

    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    def test_create_order_success(self, color):
        payload = {
            "firstName": "Test",
            "lastName": "User",
            "address": "123 Test St",
            "metroStation": "4",
            "phone": "+70000000000",
            "rentTime": 5,
            "deliveryDate": "2025-06-30",
            "comment": "Test order",
            "color": color
        }
        with allure.step("Создаём заказ с цветом: " + str(color)):
            response = requests.post(CREATE_ORDER, json=payload)
        with allure.step("Проверяем, что заказ создан"):
            assert response.status_code == HTTP_201_CREATED
            assert "track" in response.json()
