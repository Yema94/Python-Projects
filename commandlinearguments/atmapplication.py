# Assignment using Command Line Arguments
""" # ATM Application with 4 Options:
# 1)Check Balance
# 2)WithDraw
# 3)Deposit Cash
# 4)Deposit Check
"""

import sys

option = int(sys.argv[1])
remainingBalance = 10000
while True:
    print("Hello, 'Mr. Durga Rao'!\nWelcome to 'Dhiwala Bank'")
    if option==1:
        print("Your Account Balance is ",remainingBalance )
        break
    elif option==2 :
        withdraw = int(input("Please enter amount to be withdrawn : "))
        if withdraw <= remainingBalance:
            remainingBalance -=withdraw
            print(withdraw, " has been withdrawn")
            print(remainingBalance, " is remaining balance")
        else : print("Insufficient Balance")
        break
    elif option==3:
        depositCash = int(input("Please enter amount to be deposited : "))
        remainingBalance +=depositCash
        print(remainingBalance, " is remaining balance after deposit")
        break
    elif option==4:
        depositCheck = int(input("Please enter amount to be deposited through Check : "))
        remainingBalance += depositCheck
        print(remainingBalance, " is remaining balance after deposit")
        break
    else:
        option = int(input("Please enter option 1/2/3/4 only : "))
        continue
print("\nThanks and Visit again!")