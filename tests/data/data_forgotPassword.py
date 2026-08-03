def change_password_valid():
    return {
        "new_password" : "Manhdl.ptit@2026"
        }


def inf_user_valid():
    return {
        "full_name" : "Le Duc Manh",
        "phone_number" : "0397618712",
        "email" : "manhdl.ptit@gmail.com",
        "address" : "19,MP,VT,PT",
        "country" : "VN",
        "city" : "VT"
    }

def inf_user_null_not_important_value():
    return {
        "full_name" : "Le Duc Manh",
        "phone_number" : "0397618712",
        "email" : "manhdl.ptit@gmail.com",
        "address" : None,
        "country" : None,
        "city" : None
    }

def inf_user_but_wrong_fullName():
    return {
        "full_name" : "Le Duc Man",
        "phone_number" : "0397618712",
        "email" : "manhdl.ptit@gmail.com",
        "address" : "19,MP,VT,PT",
        "country" : "VN",
        "city" : "VT"
    }

def inf_user_but_wrong_phoneNumber():
    return {
        "full_name" : "Le Duc Manh",
        "phone_number" : "039761871",
        "email" : "manhdl.ptit@gmail.com",
        "address" : "19,MP,VT,PT",
        "country" : "VN",
        "city" : "VT"
    }

def inf_user_but_wrong_email():
    return {
        "full_name" : "Le Duc Manh",
        "phone_number" : "0397618712",
        "email" : "manhdl.pit@gmail.com",
        "address" : "19,MP,VT,PT",
        "country" : "VN",
        "city" : "VT"
    }


def inf_user_but_wrong_address():
    return {
        "full_name" : "Le Duc Manh",
        "phone_number" : "0397618712",
        "email" : "manhdl.ptit@gmail.com",
        "address" : "19,MP,VT,P",
        "country" : "VN",
        "city" : "VT"
    }

def inf_user_but_wrong_country():
    return {
        "full_name" : "Le Duc Manh",
        "phone_number" : "0397618712",
        "email" : "manhdl.ptit@gmail.com",
        "address" : "19,MP,VT,PT",
        "country" : "V",
        "city" : "VT"
    }

def inf_user_but_wrong_city():
    return {
        "full_name" : "Le Duc Manh",
        "phone_number" : "0397618712",
        "email" : "manhdl.ptit@gmail.com",
        "address" : "19,MP,VT,PT",
        "country" : "VN",
        "city" : "V"
    }

def inf_user_but_fullName_is_None():
    return {
        "full_name" : None,
        "phone_number" : "0397618712",
        "email" : "manhdl.ptit@gmail.com",
        "address" : "19,MP,VT,PT",
        "country" : "VN",
        "city" : "VT"
    }

def inf_user_but_phoneNumber_is_None():
    return {
        "full_name" : "Le Duc Manh",
        "phone_number" : None,
        "email" : "manhdl.ptit@gmail.com",
        "address" : "19,MP,VT,PT",
        "country" : "VN",
        "city" : "VT"
    }

def inf_user_but_email_is_None():
    return {
        "full_name" : "Le Duc Manh",
        "phone_number" : "0397618712",
        "email" : None,
        "address" : "19,MP,VT,PT",
        "country" : "VN",
        "city" : "VT"
    }

def inf_user_but_address_is_None():
    return {
        "full_name" : "Le Duc Manh",
        "phone_number" : "0397618712",
        "email" : "manhdl.ptit@gmail.com",
        "address" : None,
        "country" : "VN",
        "city" : "VT"
    }

def inf_user_but_country_is_None():
    return {
        "full_name" : "Le Duc Manh",
        "phone_number" : "0397618712",
        "email" : "manhdl.ptit@gmail.com",
        "address" : "19,MP,VT,PT",
        "country" : None,
        "city" : "VT"
    }

def inf_user_but_city_is_None():
    return {
        "full_name" : "Le Duc Manh",
        "phone_number" : "0397618712",
        "email" : "manhdl.ptit@gmail.com",
        "address" : "19,MP,VT,PT",
        "country" : "VN",
        "city" : None
    }

def inf_user_but_email_not_existed():
    return {
        "full_name" : "Le Duc Manh",
        "phone_number" : "0397618712",
        "email" : "manhdl.pit@gmail.com",
        "address" : "19,MP,VT,PT",
        "country" : "VN",
        "city" : "VT"
        }

def inf_user_but_phoneNumber_not_existed():
    return {
        "full_name" : "Le Duc Manh",
        "phone_number" : "039761872",
        "email" : "manhdl.pit@gmail.com",
        "address" : "19,MP,VT,PT",
        "country" : "VN",
        "city" : "VT"
        }
