"""
Program: Bank ATM
Author: PSUC
Date: 8th April 2026

Program Requirements: 
1. Start with pin 
2. Display menu on repeat until Exit
    2.1 Check balance
    2.2 Deposit 
    2.3 Withdraw
    2.4 Exit
3. Block account after 3 attempts of incorrect pin

Activity 3: Extend this program and add below requirements
1. Remove hardcoded dummy data 
2. Add a feature to enter customer details at program start (Name, Pin, First Deposit)
3. WHen the user sets the pin as the user to enter the pin twice and verify if both pins entered are same before continuing to register the pin.
4. WHen the user enters the first deposit amount, validate the amount and if invalid, keep giving the user another chance to enter, until the user entereas a valid amount. 
"""


#Dummy data (Hardcoded)
customerName = "Manipal"
customerPin = 6243
accountBalance = 2600000000
pinAttempt = 0
menuOpt = 0

print("---- Welcome to Sunrise Bank ----")
print("\nCustomer Name: ", customerName)

while pinAttempt<3 and menuOpt !=4:
    #Take pin input
    pin = int(input("Enter your banking PIN:"))
    #Check pin (Validation)
    if (pin == customerPin): #When pin is correct
        print("Access Granted!")

        #Loop Starts
        while True: 
            #Display Menu
            print("\n1.Check Balance \n2.Deposit \n3.Withdraw \n4.Exit")

            #Get menu choice from the user. 
            menuOpt = int(input("Enter your choice:"))

            #Check and operate the menu
            if (menuOpt == 1):
                print("Your current balance is ", accountBalance)
            elif (menuOpt == 2):
                depositAmnt = float(input("Enter amount to Deposit:"))
                #validation - Check if amount is positive
                if (depositAmnt >0):
                    accountBalance+=depositAmnt #This line is same as --> accountBalance = accountBalance + depositAmnt
                    print("Your deposit was successfull..")
                else: 
                    print("Deposit amount cannot be less than or equal to 0!")
            elif (menuOpt == 3):
                withdrawalAmnt = float(input("Enter amount to withdraw:"))
                #validation - Check if amount is positive & less than or equal to the accountBalance
                if (withdrawalAmnt > 0):
                    if(withdrawalAmnt <= accountBalance):
                        accountBalance-=withdrawalAmnt
                        print("Your withdrawal was successful..")
                    else: 
                        print("The Withdrawal amount cannot be greater than the account balance!")
                else:
                    print("Withdrawal amount cannot be less than or equal to 0!")
            elif (menuOpt == 4):
                print("Thank you for using our service...Please come back again!")
                break #Break statement used to forcefully stop a look or break out or come out of a loop..

    else: #Incase of incorrect pin
        print("Incorrect Pin..")
        pinAttempt+=1
        if(pinAttempt == 3):
            print("Your Account is blocked!")


