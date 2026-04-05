from tests.data.data_signup import signup_valid
from tests.data.data_login import *
# ddddddddd
def test_login_successfully(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json=payload_signup)
    
    data_signup = response_signup.get_json()
    token = data_signup.get("token")

    payload_login = login_valid()
    response_login = client.post("/login", json=payload_login, headers = {"Auth": f"Token {token}"})

    assert response_login.status_code == 200
    assert response_login.json == {"successfully" : "login successfully"}


# dddddd
def test_login_wrong_password(client):
    payload_signup = signup_valid()

    response_signup = client.post("/signup", json=payload_signup)

    data_signup = response_signup.get_json()
    token = data_signup.get("token")

    payload_login = login_wrong_password()

    response_login = client.post("/login", json= payload_login, headers = {"Auth": f"Token {token}"})

    assert response_login.status_code == 400
    assert response_login.json == {"error" : "wrong email/phone or password"}


# dddddddd

def test_login_with_not_token(client):
    payload_signup = signup_valid()

    response_signup = client.post("/signup", json=payload_signup)
    
    payload_login = login_valid()

    response_login = client.post("/login", json=payload_login)

    assert response_login.status_code == 400
    assert response_login.json == {"error" : "not authentic"}


# dddddddd
def test_login_email_or_phoneNumber_not_existed(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json=payload_signup)

    data_signup = response_signup.get_json()
    token = data_signup.get("token")

    payload_login = login_not_found_user()
    response_login = client.post("/login", json= payload_login, headers = {"Auth": f"Token {token}"})

    assert response_login.status_code == 400
    assert response_login.json == {"error" : "wrong email/phone or password"}

# dddddd

def test_login_with_not_input_email_or_phone_number(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json=payload_signup)

    data_signup = response_signup.get_json()
    token = data_signup.get("token")

    payload_login = login_not_input_username()

    response_login = client.post("/login", json= payload_login, headers = {"Auth": f"Token {token}"})

    assert response_login.status_code == 400
    assert response_login.json == {'error': 'must input phone_number or email'}


# ddddddddd
def test_login_with_not_input_password(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json=payload_signup)

    data_signup = response_signup.get_json()
    token = data_signup.get("token")

    payload_login = login_not_input_password()
    response_login = client.post("/login", json= payload_login, headers = {"Auth": f"Token {token}"})

    assert response_login.status_code == 400
    assert response_login.json == {'error': 'must input password'}

