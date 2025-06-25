import pytest
from utils import register_new_courier_and_return_login_password, get_courier_id, delete_courier

@pytest.fixture
def new_courier():
    login_pass, response = register_new_courier_and_return_login_password()
    courier_id = get_courier_id(login_pass[0], login_pass[1])
    yield login_pass, response
    if courier_id:
        delete_courier(courier_id)
