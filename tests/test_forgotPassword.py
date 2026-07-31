from tests.data.data_signup import signup_valid
from tests.data.data_login import (login_valid_new_password_user_choose, 
                                   login_valid_new_password_default
                                   )
from tests.data.data_forgotPassword import (forgotPassword_valid, 
                                            forgotPassword_wrong_inf,
                                            password_user_choose,
                                            forgotPassword_valid2
                                            )



def test_change_successfully(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json=payload_signup)
    data_signup = response_signup.get_json()
    token_before_change_password = data_signup.get("token")

    
    payload_forgot_password = forgotPassword_valid()
    response_forgot_password = client.post("/forgot-password", json=payload_forgot_password, headers = {"Auth": f"Token {token_before_change_password}"})
    data_forgot_password = response_forgot_password.get_json()
    token_after_change_password = data_forgot_password.get("your token")

    assert response_forgot_password.status_code == 200
    assert response_forgot_password.json == {
        "successfully" : "go to \"/new-password\" ",
        "your token" : token_after_change_password
        }

    
    payload_new_password = password_user_choose()
    response_new_password = client.put("/new-password", json=payload_new_password, headers = {"Auth": f"Token {token_after_change_password}"})
    
    assert response_new_password.status_code == 200
    assert response_new_password.json == {"successfully" : "change password successfully"}

    
    payload_login = login_valid_new_password_user_choose()
    response_login = client.post("/login", json=payload_login, headers = {"Auth": f"Token {token_after_change_password}"})

    assert response_login.status_code == 200
    assert response_login.json == {"successfully" : "login successfully"}



def test_forgotPassword_wrong_inf(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json=payload_signup)
    data_signup = response_signup.get_json()
    token_before_change_password = data_signup.get("token")

    
    payload_forgot_password = forgotPassword_wrong_inf()
    response_forgot_password = client.post("/forgot-password", json=payload_forgot_password, headers = {"Auth": f"Token {token_before_change_password}"})
    data_forgot_password = response_forgot_password.get_json()

    assert response_forgot_password.status_code == 400
    assert response_forgot_password.json == {"error" : "information is not the same"}

    
    payload_new_password = password_user_choose()
    response_new_password = client.put("/new-password", json=payload_new_password, headers = {"Auth": f"Token {token_before_change_password}"})
    
    assert response_new_password.status_code == 403
    assert response_new_password.json == {"error" : "Forbidden! You must successful in \"/forgot-password\""}



def test_login_with_password_default(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json=payload_signup)
    data_signup = response_signup.get_json()
    token_before_change_password = data_signup.get("token")

    
    payload_forgot_password = forgotPassword_valid()
    response_forgot_password = client.post("/forgot-password", json=payload_forgot_password, headers = {"Auth": f"Token {token_before_change_password}"})
    data_forgot_password = response_forgot_password.get_json()
    token_after_change_password = data_forgot_password.get("your token")

    assert response_forgot_password.status_code == 200
    assert response_forgot_password.json == {
        "successfully" : "go to \"/new-password\" ",
        "your token" : token_after_change_password
        }

   
    payload_new_password = ({

    })
    response_new_password = client.put("/new-password", json=payload_new_password, headers = {"Auth": f"Token {token_after_change_password}"})
    data_new_password = response_new_password.get_json()
    
    assert response_new_password.status_code == 200
    assert response_new_password.json == {"successfully" : "password default is \"123456789\""}
    
    
    payload_login = login_valid_new_password_default()
    response_login = client.post("/login", json=payload_login, headers = {"Auth": f"Token {token_after_change_password}"})

    assert response_login.status_code == 200
    assert response_login.json == {"successfully" : "login successfully"}



def test_with_no_url_forgotPass(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json=payload_signup)
    data_signup = response_signup.get_json()
    token_before_change_password = data_signup.get("token")
    
    
    payload_new_password = password_user_choose()
    response_new_password = client.put("/new-password", json=payload_new_password, headers = {"Auth": f"Token {token_before_change_password}"})
    
    assert response_new_password.status_code == 403
    assert response_new_password.json == {"error" : "Forbidden! You must successful in \"/forgot-password\""}


def test_username_not_signup(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json=payload_signup)
    data_signup = response_signup.get_json()
    token_before_change_password = data_signup.get("token")

    
    payload_forgot_password = forgotPassword_valid2()
    response_forgot_password = client.post("/forgot-password", json=payload_forgot_password, headers = {"Auth": f"Token {token_before_change_password}"})
    data_forgot_password = response_forgot_password.get_json()
    token_after_change_password = data_forgot_password.get("your token")

    assert response_forgot_password.status_code == 400
    assert response_forgot_password.json == {"error" : "user not sign up yet"}


def test_no_header_auth(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json=payload_signup)
    data_signup = response_signup.get_json()        
        
    payload_new_password = password_user_choose()
    response_new_password = client.put("/new-password", json=payload_new_password)
        
    assert response_new_password.status_code == 401
    assert response_new_password.json == {'error': 'not authentic'}