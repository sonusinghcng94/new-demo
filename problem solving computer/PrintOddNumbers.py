"""
Program: Print Odd numbers 
Author: PSUC
Date: 8th April 2026
"""

print("Odd numbers list: ")
for i in range(1,10):
    if(i%2!=0):
        print(i)

print("Odd numbers list (using continue): ")
for i in range(1,10):
    if(i%2==0):
        continue #Continue statement --> skips the remaining statements in a loop and moves to the next number of the loop.
    print(i)