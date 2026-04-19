# Bank ATM Program - Extended Version

print("---- Welcome to Nepal Bank ----")

# -------------------------------
# CUSTOMER REGISTRATION
# -------------------------------

# Enter customer name
customerName = input("Enter your name: ")

# Set PIN with confirmation
while True:
    pin1 = input("Set your 4-digit PIN: ")
    pin2 = input("Confirm your PIN: ")

    if pin1 == pin2:
        customerPin = int(pin1)
        print("PIN set successfully!")
        break
    else:
        print("PINs do not match. Please try again.")

# First deposit with validation
while True:
    try:
        accountBalance = float(input("Enter initial deposit amount: "))
        if accountBalance > 0:
            print("Account created successfully!")
            break
        else:
            print("Amount must be greater than 0.")
    except:
        print("Invalid input! Please enter a valid number.")

# -------------------------------
# ATM SYSTEM
# -------------------------------

pinAttempt = 0
menuOpt = 0

print("\nCustomer Name:", customerName)

while pinAttempt < 3:
    try:
        pin = int(input("Enter your banking PIN: "))
    except:
        print("Invalid PIN format.")
        continue

    if pin == customerPin:
        print("Access Granted!")

        while True:
            print("\n1. Check Balance \n2. Deposit \n3. Withdraw \n4. Exit")

            try:
                menuOpt = int(input("Enter your choice: "))
            except:
                print("Invalid choice!")
                continue

            if menuOpt == 1:
                print("Your current balance is:", accountBalance)

            elif menuOpt == 2:
                try:
                    depositAmnt = float(input("Enter amount to Deposit: "))
                    if depositAmnt > 0:
                        accountBalance += depositAmnt
                        print("Deposit successful!")
                    else:
                        print("Amount must be greater than 0!")
                except:
                    print("Invalid amount!")

            elif menuOpt == 3:
                try:
                    withdrawalAmnt = float(input("Enter amount to Withdraw: "))
                    if withdrawalAmnt > 0:
                        if withdrawalAmnt <= accountBalance:
                            accountBalance -= withdrawalAmnt
                            print("Withdrawal successful!")
                        else:
                            print("Insufficient balance!")
                    else:
                        print("Amount must be greater than 0!")
                except:
                    print("Invalid amount!")

            elif menuOpt == 4:
                print("Thank you for using our service... Please come again!")
                break

            else:
                print("Invalid option! Please select 1-4.")

        break  # Exit outer loop after successful session

    else:
        pinAttempt += 1
        print("Incorrect PIN... Attempts left:", 3 - pinAttempt)

        if pinAttempt == 3:
            print("Your Account is blocked!")