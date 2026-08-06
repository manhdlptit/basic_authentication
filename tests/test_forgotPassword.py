from tests.data.data_signup import signup_valid, sign_up_null_value_not_important
from tests.data.data_forgotPassword import (inf_user_valid, 
                                            inf_user_null_not_important_value,
                                            inf_user_with_fullname_is_whitespace,
                                            inf_user_with_email_is_whitespace,
                                            inf_user_with_phone_number_is_whitespace,
                                            inf_user_null_not_important_value
                                           )

def test_inf_valid_to_change_password(client):
    payload_signup = signup_valid()
    client.post("/signup", json = payload_signup)

    payload_inf_user = inf_user_valid()
    response_inf_user = client.post("/forgot-password", json = payload_inf_user)

    access_token = response_inf_user.json["access_token"]
    refresh_token = response_inf_user.json["refresh_token"]

    assert response_inf_user.status_code == 200
    assert response_inf_user.json == {
        "successfully" : "go to \"/change-password\"",
        "access_token" : access_token,
        "refresh_token" : refresh_token
        }



def test_inf_not_same(client):
    payload_signup = signup_valid()
    client.post("/signup", json = payload_signup)

    payload_inf_user = inf_user_null_not_important_value()
    response_inf_user = client.post("/forgot-password", json = payload_inf_user)

    assert response_inf_user.status_code == 400
    assert response_inf_user.json == {"error" : "information is not the same"}



def test_null_value_not_important_successfully(client):
    payload_signup = sign_up_null_value_not_important()
    client.post("/signup", json = payload_signup)

    payload_inf_user = inf_user_null_not_important_value()
    response_inf_user = client.post("/forgot-password", json = payload_inf_user)

    access_token = response_inf_user.json["access_token"]
    refresh_token = response_inf_user.json["refresh_token"]

    assert response_inf_user.status_code == 200
    assert response_inf_user.json == {
        "successfully" : "go to \"/change-password\"",
        "access_token" : access_token,
        "refresh_token" : refresh_token
        }



def test_inf_user_with_fullname_is_white_space(client):
    payload_forgot_password = inf_user_with_fullname_is_whitespace()
    response_forgot_password = client.post("/forgot-password", json = payload_forgot_password)

    assert response_forgot_password.status_code == 400
    assert response_forgot_password.json == {"Error" : "Missing fullname"}



def test_inf_user_with_email_is_white_space(client):
    payload_forgot_password = inf_user_with_email_is_whitespace()
    response_forgot_password = client.post("/forgot-password", json = payload_forgot_password)

    assert response_forgot_password.status_code == 400
    assert response_forgot_password.json == {"Error" : "Missing email"}



def test_inf_user_with_phone_number_is_white_space(client):
    payload_forgot_password = inf_user_with_phone_number_is_whitespace()
    response_forgot_password = client.post("/forgot-password", json = payload_forgot_password)

    assert response_forgot_password.status_code == 400
    assert response_forgot_password.json == {"Error" : "Missing phone number"}








