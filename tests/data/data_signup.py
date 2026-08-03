def signup_valid():
    return ({
        "full_name" : "Le Duc Manh",
        "phone_number" : "0397618712",
        "email" : "manhdl.ptit@gmail.com",
        "input_password" : "Lwman8_1812",
        "check_password": "Lwman8_1812",
        "address" : "19,MP,VT,PT",
        "country" : "VN",
        "city" : "VT"
    })

def sign_up_null_value_not_important():
    return ({
        "full_name" : "Le Duc Manh",
        "phone_number" : "0397618712",
        "email" : "manhdl.ptit@gmail.com",
        "input_password" : "Lwman8_1812",
        "check_password": "Lwman8_1812",
        "address" : None,
        "country" : None,
        "city" : None
    })

def signup_valid_but_same_email():
    return ({
        "full_name" : "Le Duc Manhh",
        "phone_number" : "03976187122",
        "email" : "manhdl.ptit@gmail.com",
        "input_password" : "Lwman8_18122",
        "check_password": "Lwman8_18122",
        "address" : "19,MP,VT,PTT",
        "country" : "VNN",
        "city" : "VTT"
    })

def signup_valid_but_same_phoneNumber():
    return ({
        "full_name" : "Le Duc Manhh",
        "phone_number" : "0397618712",
        "email" : "manhdl.ptitt@gmail.com",
        "input_password" : "Lwman8_18122",
        "check_password": "Lwman8_18122",
        "address" : "19,MP,VT,PTT",
        "country" : "VNN",
        "city" : "VTT"
    })

def signup_with_not_fullName():
    return ({
        "phone_number" : "0397618712",
        "email" : "manhdl.ptit@gmail.com",
        "input_password" : "Lwman8_1812",
        "check_password": "Lwman8_1812",
        "address" : "19,MP,VT,PT",
        "country" : "VN",
        "city" : "VT"
    })

def signup_with_not_phoneNumber():
    return ({
        "full_name" : "Le Duc Manh",
        "email" : "manhdl.ptit@gmail.com",
        "input_password" : "Lwman8_1812",
        "check_password": "Lwman8_1812",
        "address" : "19,MP,VT,PT",
        "country" : "VN",
        "city" : "VT"
    })

def signup_with_not_email():
    return ({
        "full_name" : "Le Duc Manh",
        "phone_number" : "0397618712",
        "input_password" : "Lwman8_1812",
        "check_password": "Lwman8_1812",
        "address" : "19,MP,VT,PT",
        "country" : "VN",
        "city" : "VT"
    })

def signup_with_not_inputPassword():
    return ({
        "full_name" : "Le Duc Manh",
        "phone_number" : "0397618712",
        "email" : "manhdl.ptit@gmail.com",
        "check_password": "Lwman8_1812",
        "address" : "19,MP,VT,PT",
        "country" : "VN",
        "city" : "VT"
    })

def signup_with_not_checkPassword():
    return ({
        "full_name" : "Le Duc Manh",
        "phone_number" : "0397618712",
        "email" : "manhdl.ptit@gmail.com",
        "input_password" : "Lwman8_1812",
        "address" : "19,MP,VT,PT",
        "country" : "VN",
        "city" : "VT"
    })

def signup_with_not_address():
    return ({
        "full_name" : "Le Duc Manh",
        "phone_number" : "0397618712",
        "email" : "manhdl.ptit@gmail.com",
        "input_password" : "Lwman8_1812",
        "check_password": "Lwman8_1812",
        "country" : "VN",
        "city" : "VT"
    })

def signup_with_not_country():
    return ({
        "full_name" : "Le Duc Manh",
        "phone_number" : "0397618712",
        "email" : "manhdl.ptit@gmail.com",
        "input_password" : "Lwman8_1812",
        "check_password": "Lwman8_1812",
        "address" : "19,MP,VT,PT",
        "city" : "VT"
    })

def signup_with_not_city():
    return ({
        "full_name" : "Le Duc Manh",
        "phone_number" : "0397618712",
        "email" : "manhdl.ptit@gmail.com",
        "input_password" : "Lwman8_1812",
        "check_password": "Lwman8_1812",
        "address" : "19,MP,VT,PT",
        "country" : "VN",
    })

def signup_two_password_not_same():
    return ({
        "full_name" : "Le Duc Manh",
        "phone_number" : "0397618712",
        "email" : "manhdl.ptit@gmail.com",
        "input_password" : "Lwman8_1812",
        "check_password": "Lwman8_181",
        "address" : "19,MP,VT,PT",
        "country" : "VN",
        "city" : "VT"
    })

def signup_password_shorter_than_8_character():
    return ({
        "full_name" : "Le Duc Manh",
        "phone_number" : "0397618712",
        "email" : "manhdl.ptit@gmail.com",
        "input_password" : "Lwm",
        "check_password": "Lwm",
        "address" : "19,MP,VT,PT",
        "country" : "VN",
        "city" : "VT"
    })

def signup_password_is_8_character():
    return ({
        "full_name" : "Le Duc Manh",
        "phone_number" : "0397618712",
        "email" : "manhdl.ptit@gmail.com",
        "input_password" : "Lwman8_1",
        "check_password": "Lwman_1",
        "address" : "19,MP,VT,PT",
        "country" : "VN",
        "city" : "VT"
    })

def signup_password_is_32_character():
    return ({
        "full_name" : "Le Duc Manh",
        "phone_number" : "0397618712",
        "email" : "manhdl.ptit@gmail.com",
        "input_password" : "Lwman8_1Lwman8_1Lwman8_1Lwman8_1",
        "check_password": "Lwman_1Lwman8_1Lwman8_1Lwman8_1",
        "address" : "19,MP,VT,PT",
        "country" : "VN",
        "city" : "VT"
    })

def signup_password_longer_than_32_character():
    return ({
        "full_name" : "Le Duc Manh",
        "phone_number" : "0397618712",
        "email" : "manhdl.ptit@gmail.com",
        "input_password" : "Lwman8_1Lwman8_1Lwman8_1Lwman8_12",
        "check_password": "Lwman_1Lwman8_1Lwman8_1Lwman8_12",
        "address" : "19,MP,VT,PT",
        "country" : "VN",
        "city" : "VT"
    })


def signup_with_password_is_8_character():
    return ({
        "full_name" : "Le Duc Manh",
        "phone_number" : "0397618712",
        "email" : "manhdl.ptit@gmail.com",
        "input_password" : "12345678",
        "check_password": "12345678",
        "address" : "19,MP,VT,PT",
        "country" : "VN",
        "city" : "VT"
    })