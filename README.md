# Sprint_7

**Описание проекта**

В этом проекте написаны автоматизированные API-тесты для учебного сервиса [Яндекс Самокат](https://qa-scooter.praktikum-services.ru/).

Используемые технологии:
- Python
- pytest
- allure-pytest
- requests

Структура проекта:
- `tests/` — директория с тестами:
  - `test_create_courier.py` — тесты на создание курьера
  - `test_login_courier.py` — тесты на логин курьера
  - `test_create_order.py` — тесты на создание заказа
  - `test_get_orders.py` — тесты на получение списка заказов
- `utils.py` — вспомогательные методы (регистрация курьера и т.д.)
- `requirements.txt` — зависимости проекта