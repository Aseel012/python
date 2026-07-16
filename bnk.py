
# BANK MANAGEMENT SYSTEM

# 1. Create Account
# 2. Deposit Money
# 3. Withdraw Money
# 4. Check Balance
# 5. Update Phone Number
# 6. Update PIN
# 7. Show Account Details
# 8. Exit

import random
import re

name = ""          # Account holder's name
acc_no = 0         # 10-digit account number
no = ""            # Phone number
pin = ""           # 4-digit PIN
bal = 0            # Current balance

def check_phoneno(phone):
    
    pattern = r'^(?:(?:\+91|0)?)[6-9]\d{9}$'
    return re.match(pattern, phone) is not None


def create_pin():
    while True:
        p = input("Create a 4-digit PIN: ")
        
        if len(p) == 4 and p.isdigit():
            return p
        else:
            print("  PIN must be exactly 4 digits. Try again.")


def get_new_phone():
  
    while True:
        new_no = input("Enter New Phone Number: ")
        
        if check_phoneno(new_no):
            return new_no
        
        print("  Invalid Phone Number. Must be a valid Indian number.")


def check_account_exists():
    
    if acc_no == 0:
        print("\n  No account found. Please create an account first.")
        return False
    return True


def verify_account():
    
    if not check_account_exists():
        return False
    
    acc = input("Enter Account Number: ")
    
    # Convert to int for comparison (acc_no is int)
    try:
        acc = int(acc)
    except ValueError:
        print("  Invalid Account Number format.")
        return False
    
    if acc == acc_no:
        return True
    else:
        print("  Invalid Account Number")
        return False


def verify_pin():
    
    if pin == "":
        print("  PIN not set. Please create an account first.")
        return False
    
    entered_pin = input("Enter PIN: ")
    
    if entered_pin == pin:
        return True
    else:
        print("  Wrong PIN")
        return False


def get_positive_amount(prompt):
    
    while True:
        try:
            amount = int(input(prompt))
            if amount <= 0:
                print("  Amount must be greater than 0.")
                continue
            return amount
        except ValueError:
            print("  Invalid input. Please enter a number.")

def create_account():
   
    global name, no, acc_no, pin, bal
    
    # Check if account already exists
    if acc_no != 0:
        print("\n  Account already exists.")
        print(f"Account Number: {acc_no}")
        return
    
    print("\n" + "="*50)
    print("        CREATE NEW ACCOUNT")
    print("="*50)
    
    # Get name
    name = input("Enter Full Name: ").strip()
    while name == "":
        print("  Name cannot be empty.")
        name = input("Enter Full Name: ").strip()
    
    # Get phone number
    while True:
        no = input("Enter Phone Number: ")
        if check_phoneno(no):
            break
        print("  Invalid Phone Number. Must be a valid Indian number.")
    
    # Generate random 10-digit account number
    acc_no = random.randint(1000000000, 9999999999)
    
    # Create PIN
    pin = create_pin()
    
    # Get initial deposit
    bal = get_positive_amount("Enter Initial Deposit (₹): ")
    
    # Display account details
    print("\n" + "="*50)
    print("        ✅ ACCOUNT CREATED SUCCESSFULLY")
    print("="*50)
    print(f"Name            : {name}")
    print(f"Account Number  : {acc_no}")
    print(f"Phone Number    : {no}")
    print(f"Current Balance : ₹{bal:,}")
    print("="*50)


def deposit():
   
    global bal
    
    # Verify account and PIN
    if not verify_account():
        return
    
    if not verify_pin():
        return
    
    print("\n" + "-"*40)
    print("        DEPOSIT MONEY")
    print("-"*40)
    
    # Get deposit amount
    dept_amt = get_positive_amount("Enter amount to deposit (₹): ")
    
    # Update balance
    bal += dept_amt
    
    print("\n✅ Deposit Successful!")
    print(f"Amount Deposited : ₹{dept_amt:,}")
    print(f"New Balance      : ₹{bal:,}")


def withdrawal():
   
    global bal
    
    # Verify account and PIN
    if not verify_account():
        return
    
    if not verify_pin():
        return
    
    print("\n" + "-"*40)
    print("        WITHDRAW MONEY")
    print("-"*40)
    
    # Get withdrawal amount
    with_amt = get_positive_amount("Enter amount to withdraw (₹): ")
    
    # Check sufficient funds
    if with_amt > bal:
        print(f"\n  Insufficient Funds!")
        print(f"Available Balance: ₹{bal:,}")
        print(f"Requested Amount : ₹{with_amt:,}")
        print(f"Shortage         : ₹{with_amt - bal:,}")
        return
    
    # Update balance
    bal -= with_amt
    
    print("\n✅ Withdrawal Successful!")
    print(f"Amount Withdrawn : ₹{with_amt:,}")
    print(f"New Balance      : ₹{bal:,}")


def balance_enquiry():
   
    if not verify_account():
        return
    
    if not verify_pin():
        return
    
    print("\n" + "-"*40)
    print("        BALANCE ENQUIRY")
    print("-"*40)
    print(f"Current Balance : ₹{bal:,}")
    print("-"*40)


def show_account_details():
    
    if not verify_account():
        return
    
    if not verify_pin():
        return
    
    print("\n" + "="*50)
    print("        ACCOUNT DETAILS")
    print("="*50)
    print(f"Name            : {name}")
    print(f"Account Number  : {acc_no}")
    print(f"Phone Number    : {no}")
    print(f"Current Balance : ₹{bal:,}")
    print("="*50)


def update_phone():
   
    global no
    
    if not check_account_exists():
        return
    
    print("\n" + "-"*40)
    print("        UPDATE PHONE NUMBER")
    print("-"*40)
    print(f"Current Phone Number: {no}")
    
    # Generate OTP
    gen_otp = random.randint(1000, 9999)
    print(f"\n📱 Generated OTP: {gen_otp} (For demo purposes)")
    
    # Verify OTP
    try:
        otp = int(input("Enter OTP: "))
    except ValueError:
        print("  Invalid OTP format.")
        return
    
    if otp != gen_otp:
        print("  Wrong OTP")
        return
    
    # Get new phone number
    new_no = get_new_phone()
    
    # Update phone number
    no = new_no
    
    print("\n✅ Phone Number Updated Successfully!")
    print(f"New Phone Number: {no}")


def update_pin():
    
    global pin
    
    if not check_account_exists():
        return
    
    print("\n" + "-"*40)
    print("        UPDATE PIN")
    print("-"*40)
    
    # Verify current PIN
    if not verify_pin():
        return
    
    # Verify phone number (last 4 digits)
    last4 = input("Enter Last 4 Digits of Phone Number: ")
    
    if last4 != no[-4:]:
        print("  Phone Number Verification Failed")
        return
    
    # Create new PIN
    print("\nCreating New PIN...")
    pin = create_pin()
    
    print("\n✅ PIN Updated Successfully!")


def update_menu():
    """
    Sub-menu for updates with switch-case implementation
    """
    while True:
        print("\n" + "-"*40)
        print("        UPDATE MENU")
        print("-"*40)
        print("1. Update Phone Number")
        print("2. Update PIN")
        print("3. Back to Main Menu")
        print("-"*40)
        
        try:
            update_choice = int(input("Enter your choice (1-3): "))
        except ValueError:
            print("  Invalid input. Please enter a number between 1 and 3.")
            continue
        
        
        match update_choice:
            case 1:
                update_phone()
            case 2:
                update_pin()
            case 3:
                print("\n↩️ Returning to Main Menu...")
                break
            case _:
                print("  Invalid choice. Please select 1, 2, or 3.")



def main():
    
    while True:
        print("\n" + "="*50)
        print("        BANK MANAGEMENT SYSTEM")
        print("="*50)
        print("1.  Create Account")
        print("2.  Deposit Money")
        print("3.  Withdraw Money")
        print("4.  Check Balance")
        print("5.  Update Details (Phone/PIN)")
        print("6.  Show Account Details")
        print("7.  Exit")
        print("="*50)
        
        try:
            choice = int(input("Enter your choice (1-7): "))
        except ValueError:
            print("  Invalid input. Please enter a number between 1 and 7.")
            continue
        
       
        match choice:
            case 1:
                create_account()
            
            case 2:
                deposit()
            
            case 3:
                withdrawal()
            
            case 4:
                balance_enquiry()
            
            case 5:
                update_menu()
            
            case 6:
                show_account_details()
            
            case 7:
                print("\n" + "="*50)
                print("        THANK YOU FOR BANKING WITH US!")
                print("="*50)
                break
            
            case _:
                print("  Invalid choice. Please select 1 to 7.")


if __name__ == "__main__":
    main()
