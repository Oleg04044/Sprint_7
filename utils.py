import random
import requests
from urls import CREATE_COURIER, LOGIN_COURIER, DELETE_COURIER

def register_new_courier_and_return_login_password():
    login = f"autotest_{random.randint(1000, 9999)}"
    password = f"pass_{random.randint(1000, 9999)}"
    first_name = f"TestName{random.randint(1000, 9999)}"
    payload = {"login": login, "password": password, "firstName": first_name}
    response = requests.post(CREATE_COURIER, json=payload)
    return (login, password, first_name), response

def get_courier_id(login, password):
    response = requests.post(LOGIN_COURIER, json={
        "login": login,
        "password": password
    })
    return response.json().get("id")

def delete_courier(courier_id):
    requests.delete(f"{DELETE_COURIER}/{courier_id}")
