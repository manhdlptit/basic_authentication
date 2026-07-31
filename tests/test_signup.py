from tests.data.data_signup import (signup_valid, 
                                    signup_with_not_phoneNumber_and_email, 
                                    signup_valid_but_same_email,
                                    signup_valid_but_same_phoneNumber,
                                    signup_two_password_not_same,
                                    signup_password_short,
                                    signup_with_password_is_8_character
                                    )

def test_sign_up_successful(client):
    payload = signup_valid()
    response = client.post("/signup", json=payload)
    data = response.get_json()


    assert response.status_code == 201
    assert data.get("email") == "manhdl.ptit@gmail.com"
    assert data.get("password") is None
    assert data.get("token") is not None



def test_sign_up_with_null_username(client):
    payload = signup_with_not_phoneNumber_and_email()
    response = client.post("/signup", json=payload)

    assert response.status_code == 400
    assert response.json == {'error': 'not null email or phone_number'}



def test_sign_up_with_email_existed(client):
    payload_signup_first_time = signup_valid()
    response_signup_first_time = client.post("/signup", json=payload_signup_first_time)

    payload_signup_second_time = signup_valid_but_same_email()
    response_signup_second_time = client.post("/signup", json=payload_signup_second_time)

    assert response_signup_second_time.status_code == 400
    assert response_signup_second_time.json == {"error" : "email existed!"}



def test_sign_up_with_phone_existed(client):
    payload_signup_first_time = signup_valid()

    response_signup_first_time = client.post("/signup", json=payload_signup_first_time)

    payload_signup_second_time = signup_valid_but_same_phoneNumber()

    response_signup_second_time = client.post("/signup", json=payload_signup_second_time)


    assert response_signup_second_time.status_code == 400
    assert response_signup_second_time.json == {"error" : "phone existed!"}



def test_two_password_different(client):
    payload = signup_two_password_not_same()

    response = client.post("/signup", json=payload)

    assert response.status_code == 400
    assert response.json == {"error" : "input password different check password"}



def test_password_short(client):
    payload = signup_password_short()

    response = client.post("/signup", json=payload)

    assert response.status_code == 400
    assert response.json == {"error" : "password must longer than 8 character"}



def test_length_password_is_8_character(client):
    payload = signup_with_password_is_8_character()

    response = client.post("/signup", json=payload)

    assert response.status_code == 201
