from tests.data.data_signup import (signup_valid,
                                    signup_with_not_phoneNumber,
                                    signup_valid_but_same_email,
                                    signup_valid_but_same_phoneNumber,
                                    signup_two_password_not_same,
                                    signup_password_shorter_than_8_character)


def test_not_null_value_successful(client):
    payload = signup_valid()
    response = client.post("/signup", json=payload)

    access_token = response.json["access_token"]
    refresh_token = response.json["refresh_token"]

    assert response.status_code == 201
    assert response.json == {"access_token" : access_token, "refresh_token" : refresh_token}



def test_null_not_important_value_successful(client):
    payload = signup_valid()
    response = client.post("/signup", json=payload)

    access_token = response.json["access_token"]
    refresh_token = response.json["refresh_token"]

    assert response.status_code == 201
    assert response.json == {"access_token" : access_token, "refresh_token" : refresh_token}



def test_null_email_and_phoneNumber(client):
    payload = signup_with_not_phoneNumber()
    response = client.post("/signup", json=payload)

    assert response.status_code == 400
    assert response.json == {"Error" : "Missing username"}



def test_email_signup_yet(client):
    payload_signup_first_time = signup_valid()
    client.post("/signup", json=payload_signup_first_time)

    payload_signup_second_time = signup_valid_but_same_email()
    response_signup_second_time = client.post("/signup", json=payload_signup_second_time)

    assert response_signup_second_time.status_code == 400
    assert response_signup_second_time.json == {"Error" : "Email existed !"}



def test_phone_number_signup_yet(client):
    payload_signup_first_time = signup_valid()

    client.post("/signup", json=payload_signup_first_time)

    payload_signup_second_time = signup_valid_but_same_phoneNumber()

    response_signup_second_time = client.post("/signup", json=payload_signup_second_time)

    assert response_signup_second_time.status_code == 400
    assert response_signup_second_time.json == {"Error" : "Phone number existed !"}



def test_two_password_not_same(client):
    payload = signup_two_password_not_same()

    response = client.post("/signup", json=payload)

    assert response.status_code == 400
    assert response.json == {"Error" : "Input password different check password"}



def test_password_short(client):
    payload = signup_password_shorter_than_8_character()

    response = client.post("/signup", json=payload)

    assert response.status_code == 400
    assert response.json == {'Error': 'Password between 8 and 32 characters'}



