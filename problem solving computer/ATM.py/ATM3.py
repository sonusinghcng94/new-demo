print("---- Welcome to Sunrise Bank ----")

# -------------------------------
# CUSTOMER DETAILS AT START
# -------------------------------
customerName = input("Enter your name: ")

# PIN confirmation
while True:
    pin1 = input("Set your PIN: ")
    pin2 = input("Confirm your PIN: ")

    if pin1 == pin2:
        customerPin = int(pin1)
        print("PIN set successfully!")
        break
    else:
        print("PINs do not match. Please try again.")

# First deposit validation loop
while True:
    try:
        accountBalance = float(input("Enter your first deposit: "))
        if accountBalance > 0:
            print("Deposit accepted!")
            break
        else:
            print("Amount must be greater than 0. Try again.")
    except:
        print("Invalid input! Please enter a number.")

# -------------------------------
# ATM SYSTEM
# -------------------------------
pinAttempt = 0
menuOpt = 0

print("\nCustomer Name:", customerName)

while pinAttempt < 3 and menuOpt != 4:
    pin = int(input("Enter your banking PIN: "))

    if (pin == customerPin):
        print("Access Granted!")

        while True:
            print("\n1.Check Balance \n2.Deposit \n3.Withdraw \n4.Exit")

            menuOpt = int(input("Enter your choice: "))

            if (menuOpt == 1):
                print("Your current balance is", accountBalance)

            elif (menuOpt == 2):
                depositAmnt = float(input("Enter amount to Deposit: "))
                if (depositAmnt > 0):
                    accountBalance += depositAmnt
                    print("Deposit successful!")
                else:
                    print("Amount must be greater than 0!")

            elif (menuOpt == 3):
                withdrawalAmnt = float(input("Enter amount to withdraw: "))
                if (withdrawalAmnt > 0):
                    if (withdrawalAmnt <= accountBalance):
                        accountBalance -= withdrawalAmnt
                        print("Withdrawal successful!")
                    else:
                        print("Insufficient balance!")
                else:
                    print("Amount must be greater than 0!")

            elif (menuOpt == 4):
                print("Thank you for using our service!")
                break

    else:
        print("Incorrect PIN..")
        pinAttempt += 1
        if (pinAttempt == 3):
            print("Your Account is blocked!")