import requests
import allure
from utils import register_new_courier_and_return_login_password

class TestLoginCourier:

    def test_login_courier_success(self):
        with allure.step("Создаём нового курьера"):
            login_pass, _ = register_new_courier_and_return_login_password()
        payload = {
            "login": login_pass[0],
            "password": login_pass[1]
        }
        with allure.step("Логинимся под курьером"):
            response = requests.post(
                'https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
                data=payload
            )
        with allure.step("Проверяем успешный логин"):
            assert response.status_code == 200, "Неверный статус при успешном логине"
            assert "id" in response.json(), "В ответе нет id курьера"

    def test_login_courier_without_required_fields(self):
        payload = {
            "login": "",
            "password": ""
        }
        with allure.step("Логинимся без обязательных значений"):
            response = requests.post(
                'https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
                data=payload
            )
        with allure.step("Проверяем ошибку при пустых значениях"):
            assert response.status_code == 400, "Ожидался статус 400 при пустых обязательных значениях"
            assert response.json()["message"] == "Недостаточно данных для входа"

    def test_login_courier_with_incorrect_data(self):
        payload = {
            "login": "nonexistent_login",
            "password": "wrong_password"
        }
        with allure.step("Логинимся с неверными данными"):
            response = requests.post(
                'https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
                data=payload
            )
        with allure.step("Проверяем ошибку неверного логина/пароля"):
            assert response.status_code == 404, "Ожидался статус 404 для несуществующего курьера"
            assert response.json()["message"] == "Учетная запись не найдена"
