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

def signup_with_not_phoneNumber_and_email():
    return ({
        "full_name" : "Le Duc Manh",
        # "phone_number" : "0397618712",
        # "email" : "manhdl.ptit@gmail.com",
        "input_password" : "Lwman8_1812",
        "check_password": "Lwman8_1812",
        "address" : "19,MP,VT,PT",
        "country" : "VN",
        "city" : "VT"
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

def signup_password_short():
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
