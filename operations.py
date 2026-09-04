from auth import users
from validation import validate_amount, validate_card_number, validate_cvv


def show_balance(username):
    print("Current Balance:", users[username]["balance"], "EGP")


def link_card(username):
    card_number = input("Enter card number: ")
    card_holder = input("Enter card holder name: ")
    expiry_date = input("Enter expiry date: ")
    cvv = input("Enter CVV: ")

    if not validate_card_number(card_number):
        print("Invalid card number.")
        return

    if not validate_cvv(cvv):
        print("Invalid CVV.")
        return

    users[username]["card"] = {
        "card_number": card_number,
        "card_holder": card_holder,
        "expiry_date": expiry_date,
        "cvv": cvv
    }

    print("Card linked successfully.")


def deposit(username):
    amount = float(input("Enter deposit amount: "))

    if not validate_amount(amount):
        print("Invalid amount.")
        return

    users[username]["balance"] += amount

    users[username]["transactions"].append({
        "type": "Deposit",
        "amount": amount
    })

    print("Deposit successful.")


def withdraw(username):
    amount = float(input("Enter withdraw amount: "))

    if not validate_amount(amount):
        print("Invalid amount.")

    elif amount > users[username]["balance"]:
        print("Insufficient balance.")

    else:
        users[username]["balance"] -= amount

        users[username]["transactions"].append({
            "type": "Withdraw",
            "amount": amount
        })

        print("Withdraw successful.")


def transfer(username):
    receiver = input("Enter receiver username: ")

    if receiver not in users:
        print("User not found.")
        return

    if receiver == username:
        print("You cannot transfer to yourself.")
        return

    amount = float(input("Enter transfer amount: "))

    if not validate_amount(amount):
        print("Invalid amount.")
        return

    if amount > users[username]["balance"]:
        print("Insufficient balance.")
        return

    confirm = input("Confirm transfer? yes/no: ")

    if confirm == "yes":
        users[username]["balance"] -= amount
        users[receiver]["balance"] += amount

        users[username]["transactions"].append({
            "type": "Transfer",
            "amount": amount,
            "to": receiver
        })

        print("Transfer successful.")

    else:
        print("Transfer cancelled.")


def show_transactions(username):
    transactions = users[username]["transactions"]

    if len(transactions) == 0:
        print("No transactions.")
        return

    for transaction in transactions:
        print(transaction)