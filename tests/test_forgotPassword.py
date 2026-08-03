from tests.data.data_signup import signup_valid, sign_up_null_value_not_important
from tests.data.data_forgotPassword import (inf_user_valid, 
                                            inf_user_but_phoneNumber_not_existed,
                                            inf_user_but_address_is_None,
                                            change_password_valid,
                                            inf_user_null_not_important_value
                                           )


def test_inf_valid_change_password_successfully(client):
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


    payload_change_password = change_password_valid()
    response_change_password = client.post("/change-password", json = payload_change_password, headers = {"Authorization" : f"Bearer {access_token}"})

    assert response_change_password.status_code == 200
    assert response_change_password.json == {"successfully" : "change password successfully"}



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



def test_access_change_password_successfully(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)

    access_token = response_signup.json["access_token"]
    refresh_token = response_signup.json["refresh_token"]

    payload_change_password = change_password_valid()
    response_change_password = client.post("/change-password", json = payload_change_password, headers = {"Authorization" : f"Bearer {access_token}"})

    assert response_change_password.status_code == 200
    assert response_change_password.json == {
            "successfully" : "change password successfully"}






