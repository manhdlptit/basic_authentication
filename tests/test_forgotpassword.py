from tests.data.data_signup import *
from tests.data.data_login import *
from tests.data.data_forgotPassword import *

# ddddddddd
def test_forgotPassword_and_change_password_successfully_and_login_with_new_password_user_choose(client):
    # signup
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json=payload_signup)
    data_signup = response_signup.get_json()
    token_before_change_password = data_signup.get("token")

    # forgot pass
    payload_forgot_password = forgotPassword_valid()
    response_forgot_password = client.post("/forgot-password", json=payload_forgot_password, headers = {"Auth": f"Token {token_before_change_password}"})
    data_forgot_password = response_forgot_password.get_json()
    token_after_change_password = data_forgot_password.get("your token")

    assert response_forgot_password.status_code == 200
    assert response_forgot_password.json == {
        "successfully" : "go to \"/new-password\" ",
        "your token" : token_after_change_password
        }

    # new pass
    payload_new_password = password_user_choose()
    response_new_password = client.put("/new-password", json=payload_new_password, headers = {"Auth": f"Token {token_after_change_password}"})
    
    assert response_new_password.status_code == 200
    assert response_new_password.json == {"successfully" : "change password successfully"}

    # login
    payload_login = login_valid_new_password_user_choose()
    response_login = client.post("/login", json=payload_login, headers = {"Auth": f"Token {token_after_change_password}"})

    assert response_login.status_code == 200
    assert response_login.json == {"successfully" : "login successfully"}


# dddddd
def test_forgotPassword_with_wrong_inf(client):
    # signup
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json=payload_signup)
    data_signup = response_signup.get_json()
    token_before_change_password = data_signup.get("token")

    # forgot pass
    payload_forgot_password = forgotPassword_wrong_inf()
    response_forgot_password = client.post("/forgot-password", json=payload_forgot_password, headers = {"Auth": f"Token {token_before_change_password}"})
    data_forgot_password = response_forgot_password.get_json()

    assert response_forgot_password.status_code == 400
    assert response_forgot_password.json == {"error" : "information is not the same"}

    # new pass
    payload_new_password = password_user_choose()
    response_new_password = client.put("/new-password", json=payload_new_password, headers = {"Auth": f"Token {token_before_change_password}"})
    
    assert response_new_password.status_code == 403
    assert response_new_password.json == {"error" : "Forbidden! You must successful in \"/forgot-password\""}


# dddddddddddd
def test_forgotPassword_and_not_input_new_password_and_login_with_password_default(client):
    # signup
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json=payload_signup)
    data_signup = response_signup.get_json()
    token_before_change_password = data_signup.get("token")

    # forgot pass
    payload_forgot_password = forgotPassword_valid()
    response_forgot_password = client.post("/forgot-password", json=payload_forgot_password, headers = {"Auth": f"Token {token_before_change_password}"})
    data_forgot_password = response_forgot_password.get_json()
    token_after_change_password = data_forgot_password.get("your token")

    assert response_forgot_password.status_code == 200
    assert response_forgot_password.json == {
        "successfully" : "go to \"/new-password\" ",
        "your token" : token_after_change_password
        }

    # new pass
    payload_new_password = ({

    })
    response_new_password = client.put("/new-password", json=payload_new_password, headers = {"Auth": f"Token {token_after_change_password}"})
    data_new_password = response_new_password.get_json()
    
    assert response_new_password.status_code == 200
    assert response_new_password.json == {"successfully" : "password default is \"123456789\""}
    
    # login
    payload_login = login_valid_new_password_default()
    response_login = client.post("/login", json=payload_login, headers = {"Auth": f"Token {token_after_change_password}"})

    assert response_login.status_code == 200
    assert response_login.json == {"successfully" : "login successfully"}


# ddddddddd
def test_forgotPassword_and_change_password_with_no_url_forgotPass_before(client):
    # signup
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json=payload_signup)
    data_signup = response_signup.get_json()
    token_before_change_password = data_signup.get("token")
    
    # new pass
    payload_new_password = password_user_choose()
    response_new_password = client.put("/new-password", json=payload_new_password, headers = {"Auth": f"Token {token_before_change_password}"})
    
    assert response_new_password.status_code == 403
    assert response_new_password.json == {"error" : "Forbidden! You must successful in \"/forgot-password\""}
    