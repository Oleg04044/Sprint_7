import requests
import allure
from utils import register_new_courier_and_return_login_password

class TestCreateCourier:

    def test_create_courier_success(self):
        with allure.step("Создаём нового курьера"):
            login_pass, response = register_new_courier_and_return_login_password()
        with allure.step("Проверяем, что курьер создан"):
            assert len(login_pass) > 0, "Курьер не создался"
            assert response.status_code == 201, "Неверный статус ответа"
            assert response.json()["ok"] is True, "Ответ не содержит {'ok': true}"

    def test_create_duplicate_courier(self):
        with allure.step("Создаём курьера"):
            login_pass, _ = register_new_courier_and_return_login_password()
        payload = {
            "login": login_pass[0],
            "password": login_pass[1],
            "firstName": login_pass[2]
        }
        with allure.step("Пробуем создать дубликат"):
            duplicate_response = requests.post(
                'https://qa-scooter.praktikum-services.ru/api/v1/courier',
                data=payload
            )
        with allure.step("Проверяем ошибку дубликата"):
            assert duplicate_response.status_code == 409, "Ожидался статус 409 при повторном создании курьера"
            assert duplicate_response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    def test_create_courier_without_required_fields(self):
        payload = {}
        with allure.step("Пробуем создать курьера без обязательных полей"):
            response = requests.post(
                'https://qa-scooter.praktikum-services.ru/api/v1/courier',
                data=payload
            )
        with allure.step("Проверяем ошибку отсутствия полей"):
            assert response.status_code == 400, "Ожидался статус 400 при отсутствии обязательных полей"
            assert response.json()["message"] == "Недостаточно данных для создания учетной записи"
