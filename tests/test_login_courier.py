import requests
import allure
from data import *
from urls import LOGIN_COURIER

class TestLoginCourier:

    def test_login_success(self, new_courier):
        login_pass, _ = new_courier
        payload = {"login": login_pass[0], "password": login_pass[1]}
        with allure.step("Вход с корректными данными"):
            response = requests.post(LOGIN_COURIER, json=payload)
        with allure.step("Проверяем успешный вход"):
            assert response.status_code == HTTP_200_OK
            assert "id" in response.json()

    def test_login_with_wrong_data(self):
        payload = {"login": "wrong", "password": "wrong"}
        with allure.step("Вход с некорректными данными"):
            response = requests.post(LOGIN_COURIER, json=payload)
        with allure.step("Проверяем ошибку"):
            assert response.status_code == HTTP_404_NOT_FOUND
            assert response.json()["message"] == LOGIN_INCORRECT

    def test_login_without_required_fields(self):
        payload = {"login": "", "password": ""}
        with allure.step("Вход с пустыми полями"):
            response = requests.post(LOGIN_COURIER, json=payload)
        with allure.step("Проверка ошибки валидации"):
            assert response.status_code == HTTP_400_BAD_REQUEST
            assert response.json()["message"] == LOGIN_INCOMPLETE
