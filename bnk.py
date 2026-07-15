# PY PROGRAM FOR BANK MANAGEMENT SYSTEM
# create
# update phone
# update pin
# deposit
# withdrawal
# balance
# exit

import random
import re

# Global Variables
name = ""
no = ""
pin = ""
bal = 0
acc_no = 0


def check_phoneno(no):
    pattern = r'^(?:(?:\+91|0)?)[6-9]\d{9}$'
    return re.match(pattern, no) is not None


def create_pin():
    while True:
        p = input("Create a 4-digit PIN: ")

        if len(p) == 4 and p.isdigit():
            return p
        else:
            print("PIN must be exactly 4 digits.")


def get_new_phone():
    while True:
        new_no = input("Enter the New Phone Number: ")

        if check_phoneno(new_no):
            return new_no

        print("Invalid Phone Number. Try Again.")


def update_phno():
    global no

    if no == "":
        print("Please create an account first.")
        return

    print("Current Phone Number:", no)

    gen_otp = random.randint(1000, 9999)
    print("Generated OTP:", gen_otp)

    otp = int(input("Enter OTP: "))

    if otp == gen_otp:
        no = get_new_phone()
        print("Phone Number Updated Successfully.")
    else:
        print("Wrong OTP")


def update_pin():
    global pin

    if pin == "":
        print("Please create an account first.")
        return

    old_pin = input("Enter Current PIN: ")

    if old_pin != pin:
        print("Incorrect PIN")
        return

    last4 = input("Enter Last 4 Digits of Phone Number: ")

    if last4 != no[-4:]:
        print("Phone Number Verification Failed")
        return

    pin = create_pin()

    print("PIN Updated Successfully")


# ==========================
# MAIN MENU
# ==========================

while True:

    print("\n------- BANK -------")
    print("1. Create Account")
    print("2. Update Phone Number")
    print("3. Update PIN")
    print("4. Deposit")
    print("5. Withdrawal")
    print("6. Balance")
    print("7. Exit")

    ch = int(input("Enter Choice: "))

    match ch:

        case 1:

            if no != "":
                print("Account Already Exists")
                continue

            name = input("Enter Full Name: ")

            while True:

                no = input("Enter Phone Number: ")

                if check_phoneno(no):

                    acc_no = random.randint(1000000000, 9999999999)

                    pin = create_pin()

                    print("\nACCOUNT CREATED SUCCESSFULLY")
                    print("Account Number :", acc_no)
                    print("Phone Number   :", no)

                    break

                else:
                    print("Invalid Phone Number")

        case 2:
            update_phno()

        case 3:
            update_pin()

        case 4:
            print("Deposit - To be implemented")

        case 5:
            print("Withdrawal - To be implemented")

        case 6:
            print("Current Balance :", bal)

        case 7:
            print("Thank You")
            break

        case _:
            print("Invalid Choice")