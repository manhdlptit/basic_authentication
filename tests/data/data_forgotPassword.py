def password_change_first_time():
    return {
        "current_password" : "Lwman8_1812",
        "new_password" : "Manhdl.ptit@2026"
        }


def change_password_first_time_but_current_password_wrong():
    return {
        "current_password" : "Lwman8_181",
        "new_password" : "Manhdl.ptit@2026"
        }


def password_change_second_time():
    return {
        "current_password" : "Manhdl.ptit@2026",
        "new_password" : "leducmanh1812"
        }


def password_change_third_time():
    return {
        "current_password" : "leducmanh1812",
        "new_password" : "kichu18122007"
        }


def password_change_third_time_same_like_first_time():
    return {
    "current_password" : "leducmanh1812",
    "new_password" : "Manhdl.ptit@2026"
        }


def password_change_fourth_time():
    return {
        "current_password" : "kichu18122007",
        "new_password" : "Lwman8_1812"
    }

def password_same_like_full_name():
    return {
        "current_password" : "Lwman8_1812",
        "new_password" : "lEdUcMaNh"
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


def inf_user_but_email_not_exsited():
    return {
        "full_name" : "Le Duc Manh",
        "phone_number" : "0397618712",
        "email" : "manhdl.pit@gmail.com",
        "address" : "19,MP,VT,PT",
        "country" : "VN",
        "city" : "VT"
        }


def inf_user_but_phoneNumber_not_exsited():
    return {
        "full_name" : "Le Duc Manh",
        "phone_number" : "039761872",
        "email" : "manhdl.pit@gmail.com",
        "address" : "19,MP,VT,PT",
        "country" : "VN",
        "city" : "VT"
        }