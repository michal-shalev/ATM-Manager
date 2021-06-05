from UserAuthentication import UserAuthentication
from ATMManager import ATMManager
import time


user_auth = UserAuthentication()
atm = ATMManager()


def get_user():
    failed_attempts = 0
    while failed_attempts <= 3:
        if failed_attempts == 3:
            print("Too many failed login attempts, wait for 30 seconds until you can try again.")
            time.sleep(30)
            failed_attempts = 0
            continue

        user_account_ID = input("Please enter your account ID: ")
        user_password = input("Please enter your password: ")

        if not user_auth.isAccountIDExists(user_account_ID):
            print("Account ID doesn't exist, please try again")
            failed_attempts += 1
            continue

        authentication = user_auth.authentication(user_account_ID, user_password)
        if not authentication:
            print("Wrong password, please try again.")
            failed_attempts += 1
            continue

        print("Login successful!\n")
        failed_attempts = 0
        break

    return user_account_ID

def handle_action(user_account_id):
    try:
        action = input("Please enter your selection from the list below:\n"
                       "Balance Check - Press 1\n"
                       "Cash Withdrawal - Press 2\n"
                       "Cash Deposit - Press 3\n")
        if action == "1":
            print(f"Your balance is: {atm.get_balance(user_account_id):.2f}")

        if action == "2":
            cash_amount = input("Please enter the amount of cash you would like to withdrawal: ")
            print(
                f"Please collect your cash, your new balance is: {atm.cash_withdrawal(user_account_id, cash_amount):.2f}")

        if action == "3":
            cash_amount = input("Please enter the amount of cash you would like to deposit: ")
            print("Please insert your cash")
            time.sleep(3)
            print(f"Your new balance is: {atm.cash_deposit(user_account_id, cash_amount):.2f}.")
    except ValueError as e:
        print("Invalid value")


while True:
    print("Welcome, this is an ATM! \n")

    if input("press 'exit' if you want to exit, and anything else otherwise") == "exit":
        break
    user_account_ID = get_user()
    user_name = atm.get_user_detail(user_account_ID, "name")
    print("Welcome " + user_name)
    time.sleep(1)
    handle_action(user_account_ID)

atm.save()
