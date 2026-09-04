from validation import validate_username, validate_password, validate_phone


users = {}


def register():
    name = input("Enter full name: ")
    phone = input("Enter phone number: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if not validate_phone(phone):
        print("Invalid phone number.")
        return

    if not validate_username(username):
        print("Invalid username.")
        return

    if username in users:
        print("Username already exists.")
        return

    if not validate_password(password):
        print("Password must be at least 6 characters.")
        return

    users[username] = {
        "name": name,
        "phone": phone,
        "password": password,
        "balance": 0,
        "card": None,
        "transactions": []
    }

    print("Registration successful!")


    print("Invalid username or password.")
    return None

def login():
    attempts = 3

    while attempts > 0:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in users:
            if users[username]["password"] == password:
                print("Login successful!")
                print("Welcome", users[username]["name"])
                return username

        attempts -= 1
        print("Invalid username or password.")
        print("Attempts left:", attempts)

    print("Too many failed attempts.")
    return None