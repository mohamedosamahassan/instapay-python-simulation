from auth import register, login
from operations import (
    show_balance,
    link_card,
    deposit,
    withdraw,
    transfer,
    show_transactions
)


while True:
    print("\n===== InstaPay =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        register()

    elif choice == "2":
        current_user = login()

        if current_user != None:

            while True:
                print("\n===== Main Menu =====")
                print("1. View Balance")
                print("2. Link Card")
                print("3. Deposit")
                print("4. Withdraw")
                print("5. Transfer")
                print("6. Transaction History")
                print("7. Logout")

                user_choice = input("Choose: ")

                if user_choice == "1":
                    show_balance(current_user)

                elif user_choice == "2":
                    link_card(current_user)

                elif user_choice == "3":
                    deposit(current_user)

                elif user_choice == "4":
                    withdraw(current_user)

                elif user_choice == "5":
                    transfer(current_user)

                elif user_choice == "6":
                    show_transactions(current_user)

                elif user_choice == "7":
                    print("Logged out.")
                    break

                else:
                    print("Invalid choice.")

    elif choice == "3":
        print("Goodbye")
        break

    else:
        print("Invalid choice.")