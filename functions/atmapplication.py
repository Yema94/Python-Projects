# Assignment using Command Line Arguments
""" # TM Application with 4 Options:
# 1)Check Balance
# 2)WithDraw
# 3)Deposit Cash
# 4)Deposit Check
"""

import sys

option = int(sys.argv[1])
remainingBalance = 10000


def welcome_message():
    print("\nHello, 'Mr. Durga Rao'!\nWelcome to 'Dhiwala Bank'\n")


def exit_message():
    print("\nThanks and Visit again!\n")


def update_balance(operation, a):
    if operation == "add":
        return remainingBalance + a
    else:
        return remainingBalance - a


welcome_message()
while True:
    if option == 1:
        print("Your Account Balance is ", remainingBalance)
        break
    elif option == 2:
        withdraw = int(input("Please enter amount to be withdrawn : "))
        if withdraw <= remainingBalance:
            # remainingBalance -=withdraw
            remainingBalance = update_balance("sub", withdraw)
            print(withdraw, " has been withdrawn")
            print(remainingBalance, " is remaining balance")
        else:
            print("Insufficient Balance! Please try again... \n")
            option = 2
            continue
        break
    elif option == 3:
        depositCash = int(input("Please enter amount to be deposited : "))
        # remainingBalance +=depositCash
        remainingBalance = update_balance("add", depositCash)
        print(remainingBalance, " is remaining balance after deposit")
        break
    elif option == 4:
        depositCheck = int(input("Please enter amount to be deposited through Check : "))
        # remainingBalance += depositCheck
        remainingBalance = update_balance("add", depositCheck)
        print(remainingBalance, " is remaining balance after deposit")
        break
    else:
        option = int(input("Please enter option 1/2/3/4 only : "))
        continue
exit_message()
