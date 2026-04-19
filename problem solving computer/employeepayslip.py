""""
The problem:
Take below inputs from the user 
-Basic salary 
-Monthly allowances
-No. of days worked 
-Bonus Amount 
calculate gross salary and generate a pay slip

"""
# employee payslip program
print("Employee payslip program")

# step 1: take all input from the user 
print("Enter below details:")
employee = input("enter employee name:")
basicSal = float(input("enter the basic salary:"))
monthlyAlw = float(input("Monthly Allowances:"))
nofwrkdays = int(input("no. of days worked:"))
bonusAmt = float(input("Bonus Amount:"))

# variables needed
grossSalary = 0.0
TaxAmount = 0.0
taxRate = 0
salaryAfterTax = 0.0
NetSalary = 0.0
#validations
if(basicSal<0):
    print("Basic Salary cannot be negative!")

elif(nofwrkdays <0 or nofwrkdays >20):
    print("NO. of work days have to be between 0 to 20!")

elif(bonusAmt <0):
    print("Bonus amount cannot be negative!")
else: # all is valid..calculate the salary!
    # calculate basic salary based on no.of days worked 
    grossSalary = (basicSal/20) * nofwrkdays
    # calculate the tax amount 
    if(basicSal > 10000):
        TaxAmount = (grossSalary * 30) /100
    else:
        TaxAmount = (grossSalary * 20)/100

# calculate the net salary 
NetSalary = (grossSalary-TaxAmount) + bonusAmt

# generate the pay slip 
print("_____pay slip____")
print("Employee name:", employee)
print("--salary breakdown--")
print("Basic Salary ")
