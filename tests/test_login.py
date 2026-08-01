from tests.data.data_signup import signup_valid
from tests.data.data_login import (login_valid, 
                                   login_wrong_password,
                                   login_not_found_user,
                                   login_not_input_username,
                                   login_not_input_password
                                   )

def test_login_successfully(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json=payload_signup)
    
    data_signup = response_signup.get_json()
    token = data_signup.get("token")

    payload_login = login_valid()
    response_login = client.post("/login", json=payload_login, headers = {"Auth": f"Token {token}"})

    assert response_login.status_code == 200
    assert response_login.json == {"successfully" : "login successfully"}



def test_login_wrong_password(client):
    payload_signup = signup_valid()

    response_signup = client.post("/signup", json=payload_signup)

    data_signup = response_signup.get_json()
    token = data_signup.get("token")

    payload_login = login_wrong_password()

    response_login = client.post("/login", json= payload_login, headers = {"Auth": f"Token {token}"})

    assert response_login.status_code == 400
    assert response_login.json == {"error" : "wrong email/phone or password"}



def test_login_with_not_token(client):
    payload_signup = signup_valid()

    client.post("/signup", json=payload_signup)
    
    payload_login = login_valid()

    response_login = client.post("/login", json=payload_login)

    assert response_login.status_code == 401
    assert response_login.json == {"error" : "not authentic"}



def test_login_username_not_existed(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json=payload_signup)

    data_signup = response_signup.get_json()
    token = data_signup.get("token")

    payload_login = login_not_found_user()
    response_login = client.post("/login", json= payload_login, headers = {"Auth": f"Token {token}"})

    assert response_login.status_code == 400
    assert response_login.json == {"error" : "wrong email/phone or password"}



def test_login_null_username(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json=payload_signup)

    data_signup = response_signup.get_json()
    token = data_signup.get("token")

    payload_login = login_not_input_username()

    response_login = client.post("/login", json= payload_login, headers = {"Auth": f"Token {token}"})

    assert response_login.status_code == 400
    assert response_login.json == {'error': 'must input phone_number or email'}



def test_login_null_password(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json=payload_signup)

    data_signup = response_signup.get_json()
    token = data_signup.get("token")

    payload_login = login_not_input_password()
    response_login = client.post("/login", json= payload_login, headers = {"Auth": f"Token {token}"})

    assert response_login.status_code == 400
    assert response_login.json == {'error': 'must input password'}



def test_login_wrong_format_token(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json=payload_signup)

    data_signup = response_signup.get_json()
    token = data_signup.get("token")

    payload_login = login_valid()
    response_login = client.post("/login", json= payload_login, headers = {"Authentication": f"Baber {token}"})

    assert response_login.status_code == 401
    assert response_login.json == {'error': 'not authentic'}



def test_login_token_wrong(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json=payload_signup)

    data_signup = response_signup.get_json()
    token = data_signup.get("token")

    payload_login = login_valid()
    response_login = client.post("/login", json= payload_login, headers = {"Auth": f"Token {token}k"})

    assert response_login.status_code == 401
    assert response_login.json == {'error': 'not authentic'}