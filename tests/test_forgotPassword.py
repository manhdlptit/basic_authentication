from tests.data.data_signup import *
from tests.data.data_login import *
from tests.data.data_forgotPassword import *


def test_change_password_not_with_access_token_and_valid_data_and_successfully(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)

    payload_inf_user = inf_user_valid()
    response_inf_user = client.post("/forgot-password", json = payload_inf_user)

    access_token = response_inf_user.json["your_access_token"]

    payload_change_password = change_password_valid()
    response_change_password = client.post("/change-password", json = payload_change_password, headers = {"Authorization" : f"Bearer {access_token}"})

    assert response_change_password.status_code == 200
    assert response_change_password.json == {"successfully" : "change password successfully"}



def test_change_password_not_with_access_token_and_invalid_data_inf_not_same(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)

    payload_inf_user = inf_user_but_phoneNumber_not_exsited()
    response_inf_user = client.post("/forgot-password", json = payload_inf_user)

    assert response_inf_user.status_code == 400
    assert response_inf_user.json == {"error" : "information is not the same"}



def test_change_password_not_with_access_token_and_invalid_data_and_inf_having_null_value(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)

    payload_inf_user = inf_user_but_address_is_None()
    response_inf_user = client.post("/forgot-password", json = payload_inf_user)

    assert response_inf_user.status_code == 400
    assert response_inf_user.json == {"Error" : "Not null any value"}


def test_change_password_with_access_token_and_successfully(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)

    access_token = response_signup.json["access_token"]

    payload_change_password = change_password_valid()
    response_change_password = client.post("/change-password", json = payload_change_password, headers = {"Authorization" : f"Bearer {access_token}"})

    assert response_change_password.status_code == 200
    assert response_change_password.json == {"successfully" : "change password successfully"}