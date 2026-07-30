from tests.data.data_signup import *


def test_sign_up_with_successful(client):
    payload = signup_valid()
    response = client.post("/signup", json=payload)

    access_token = response.json["access_token"]
    re_fresh_token = response.json["re_fresh_token"]

    assert response.status_code == 201
    assert response.json == {"access_token" : access_token, "re_fresh_token" : re_fresh_token}



def test_sign_up_with_not_email_and_phoneNumber(client):
    payload = signup_with_not_phoneNumber()
    response = client.post("/signup", json=payload)

    assert response.status_code == 400
    assert response.json == {"Error" : "Not null any value"}



def test_sign_up_with_email_existed(client):
    payload_signup_first_time = signup_valid()
    response_signup_first_time = client.post("/signup", json=payload_signup_first_time)

    payload_signup_second_time = signup_valid_but_same_email()
    response_signup_second_time = client.post("/signup", json=payload_signup_second_time)

    assert response_signup_second_time.status_code == 400
    assert response_signup_second_time.json == {"Error" : "Email exsited !"}



def test_sign_up_with_phone_existed(client):
    payload_signup_first_time = signup_valid()

    response_signup_first_time = client.post("/signup", json=payload_signup_first_time)

    payload_signup_second_time = signup_valid_but_same_phoneNumber()

    response_signup_second_time = client.post("/signup", json=payload_signup_second_time)


    assert response_signup_second_time.status_code == 400
    assert response_signup_second_time.json == {"Error" : "Phone number exsited !"}



def test_sign_up_with_inputPassword_different_checkPassword(client):
    payload = signup_two_password_not_same()

    response = client.post("/signup", json=payload)

    assert response.status_code == 400
    assert response.json == {"Error" : "Input password different check password"}



def test_sign_up_with_length_password_shorter_than_8_character(client):
    payload = signup_password_shorter_than_8_character()

    response = client.post("/signup", json=payload)

    assert response.status_code == 400
    assert response.json == {'Error': 'Password between 8 and 32 characters'}



