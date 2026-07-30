def login_with_email_and_login_valid():
    return {
        "email" : "manhdl.ptit@gmail.com",
        "password" : "Lwman8_1812"
    }

def login_with_phoneNumber_and_login_valid():
    return {
        "phone_number" : "0397618712",
        "password" : "Lwman8_1812"
    }

def login_with_phoneNumber_but_wrong_password():
    return {
        "phone_number" : "0397618712",
        "password" : "Lwman8_181"
    }

def login_with_email_but_wrong_password():
    return {
        "email" : "manhdl.ptit@gmail.com",
        "password" : "Lwman8_181"
    }

def login_with_email_is_null():
    return {
        "email" : None,
        "password" : "Lwman8_181"
    }

def login_with_phoneNumber_is_null():
    return {
        "phone_number" : None,
        "password" : "Lwman8_181"
    }

def login_with_email_and_password_is_null():
    return {
        "email" : "manhdl.ptit@gmail.com",
        "password" : None
    }

def login_with_phoneNumber_and_password_is_null():
    return {
        "phone_number" : "0397618712",
        "password" : None
    }

def login_with_phoneNumber_not_exsited_in_DB():
    return {
        "phone_number" : "039761871",
        "password" : "Lwman8_1812"
    }

def login_with_email_not_exsited_in_DB():
    return {
        "email" : "manhdl.pti@gmail.com",
        "password" : "Lwman8_1812"
    }