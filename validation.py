def valid_menu_choice(choice):
    return choice in ["1", "2", "3"]


def validate_username(username):
    return len(username) >= 4


def validate_password(password):
    return len(password) >= 6


def validate_phone(phone):
    
 return phone.isdigit() and len(phone) == 11
def validate_amount(amount):
    return amount > 0


def validate_card_number(card_number):
    return card_number.isdigit() and len(card_number) == 16


def validate_cvv(cvv):
    return cvv.isdigit() and len(cvv) == 3