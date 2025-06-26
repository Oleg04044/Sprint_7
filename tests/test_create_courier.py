import requests
import allure
from data import *
from urls import CREATE_COURIER
from utils import register_new_courier_and_return_login_password

class TestCreateCourier:

    def test_create_courier_success(self):
        with allure.step("Создаём нового курьера"):
            login_pass, response = register_new_courier_and_return_login_password()
        with allure.step("Проверяем успешное создание"):
            assert len(login_pass) > 0
            assert response.status_code == HTTP_201_CREATED
            assert response.json().get("ok") is True

    def test_create_duplicate_courier(self, new_courier):
        login_pass, _ = new_courier
        payload = {
            "login": login_pass[0],
            "password": login_pass[1],
            "firstName": login_pass[2]
        }
        with allure.step("Создаём дубликата"):
            response = requests.post(CREATE_COURIER, json=payload)
        with allure.step("Проверяем ошибку дубликата"):
            assert response.status_code == HTTP_409_CONFLICT
            assert response.json()["message"] == DUPLICATE_MESSAGE

    def test_create_courier_without_required_fields(self):
        payload = {}
        with allure.step("Создание без обязательных полей"):
            response = requests.post(CREATE_COURIER, json=payload)
        with allure.step("Проверка кода ошибки"):
            assert response.status_code == HTTP_400_BAD_REQUEST
            assert response.json()["message"] == CREATE_COURIER_ERROR
