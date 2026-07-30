def login_valid():
    return({
        "phone_number" : "0397618712",
        "email" : "manhdl.ptit@gmail.com",
        "input_password" : "Lwman8_1812"
    })

def login_wrong_password():
    return({
        "phone_number" : "0397618712",
        "email" : "manhdl.ptit@gmail.com",
        "input_password" : "Lwman8_181"
    })

def login_not_found_user():
    return({
        "phone_number" : "039761871",
        "email" : "manhdl.tit@gmail.com",
        "input_password" : "Lwman8_1812"
    })

def login_not_input_username():
    return({
        "input_password" : "Lwman8_1812"
    })

def login_not_input_password():
    return({
        "phone_number" : "039761871",
        "email" : "manhdl.tit@gmail.com"
        # "input_password" : "Lwman8_1812"
    })

def login_valid_new_password_default():
    return({
        "phone_number" : "0397618712",
        "email" : "manhdl.ptit@gmail.com",
        "input_password" : "123456789"
    })

def login_valid_new_password_user_choose():
    return({
        "phone_number" : "0397618712",
        "email" : "manhdl.ptit@gmail.com",
        "input_password" : "12345678910"
    })