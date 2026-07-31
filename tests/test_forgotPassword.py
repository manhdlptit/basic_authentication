from tests.data.data_signup import signup_valid
from tests.data.data_forgotPassword import (inf_user_valid, 
                                            current_password_default,
                                            inf_user_but_phoneNumber_not_existed,
                                            inf_user_but_address_is_None,
                                            change_password_valid,
                                            current_password_wrong)


def test_inf_valid_change_password_successfully(client):
    payload_signup = signup_valid()
    client.post("/signup", json = payload_signup)

    payload_inf_user = inf_user_valid()
    response_inf_user = client.post("/forgot-password", json = payload_inf_user)

    access_token = response_inf_user.json["your_access_token"]
    re_fresh_token = response_inf_user.json["your_refresh_token"]

    assert response_inf_user.status_code == 200
    assert response_inf_user.json == {
        "successfully" : "go to \"/change-password\" with password default is '12345678' ",

        "your_access_token" : access_token,
        "your_refresh_token" : re_fresh_token
        }


    payload_change_password = current_password_default()
    response_change_password = client.post("/change-password", json = payload_change_password, headers = {"Authorization" : f"Bearer {access_token}"})

    assert response_change_password.status_code == 200
    assert response_change_password.json == {"successfully" : "change password successfully"}



def test_inf_not_same(client):
    payload_signup = signup_valid()
    client.post("/signup", json = payload_signup)

    payload_inf_user = inf_user_but_phoneNumber_not_existed()
    response_inf_user = client.post("/forgot-password", json = payload_inf_user)

    assert response_inf_user.status_code == 400
    assert response_inf_user.json == {"error" : "information is not the same"}



def test_inf_null_value(client):
    payload_signup = signup_valid()
    client.post("/signup", json = payload_signup)

    payload_inf_user = inf_user_but_address_is_None()
    response_inf_user = client.post("/forgot-password", json = payload_inf_user)

    assert response_inf_user.status_code == 400
    assert response_inf_user.json == {"Error" : "Not null any value"}



def test_access_change_password_successfully(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)

    access_token = response_signup.json["access_token"]

    payload_change_password = change_password_valid()
    response_change_password = client.post("/change-password", json = payload_change_password, headers = {"Authorization" : f"Bearer {access_token}"})

    assert response_change_password.status_code == 200
    assert response_change_password.json == {"successfully" : "change password successfully"}



def test_current_password_wrong(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)

    access_token = response_signup.json["access_token"]

    payload_change_password = current_password_wrong()
    response_change_password = client.post("/change-password", json = payload_change_password, headers = {"Authorization" : f"Bearer {access_token}"})

    assert response_change_password.status_code == 400
    assert response_change_password.json == {"Error" : "Password current not correct"}


