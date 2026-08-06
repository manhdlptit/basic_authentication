def login_with_email_and_login_valid():
    return {
        "username" : "manhdl.ptit@gmail.com",
        "password" : "Lwman8_1812"
    }


def login_with_phoneNumber_and_login_valid():
    return {
        "username" : "0397618712",
        "password" : "Lwman8_1812"
    }


def login_with_phoneNumber_but_wrong_password():
    return {
        "username" : "0397618712",
        "password" : "Lwman8_181"
    }


def login_with_email_but_wrong_password():
    return {
        "username" : "manhdl.ptit@gmail.com",
        "password" : "Lwman8_181"
    }


def login_with_email_is_null():
    return {
        "email" : None,
        "password" : "Lwman8_181"
    }


def login_with_phoneNumber_is_null():
    return {
        "username" : None,
        "password" : "Lwman8_181"
    }


def login_with_email_and_password_is_null():
    return {
        "username" : "manhdl.ptit@gmail.com",
        "password" : None
    }


def login_with_phoneNumber_and_password_is_null():
    return {
        "username" : "0397618712",
        "password" : None
    }


def login_with_phoneNumber_not_existed_in_DB():
    return {
        "username" : "039761871",
        "password" : "Lwman8_1812"
    }


def login_with_email_not_existed_in_DB():
    return {
        "username" : "manhdl.pti@gmail.com",
        "password" : "Lwman8_1812"
    }


def login_with_username_is_whitespace():
    return {
        "username" : "        ",
        "password" : "Lwman8_1812"
    }


def login_with_password_is_whitespace():
    return {
        "username" : "manhdl.pti@gmail.com",
        "password" : "        "
    }


def login_with_password_change_first_time():
    return {
        "username" : "manhdl.ptit@gmail.com",
        "password" : "Manhdl.ptit@2026"
    }


def login_with_password_change_second_time():
    return {
        "username" : "manhdl.ptit@gmail.com",
        "password" : "leducmanh1812"
    }


def login_with_password_change_third_time():
    return {
        "username" : "manhdl.ptit@gmail.com",
        "password" : "kichu18122007"
    }


def login_with_password_change_fourth_time():
    return {
        "username" : "manhdl.ptit@gmail.com",
        "password" : "Lwman8_1812"
    }

