# Program to check if a given number is prime or not
import sys
num = int(input("Enter a number : "))
primeFlag = True
for i in range(2,num):
    if num%i == 0 :
        print("{} is not a prime number(divisible by {})".format(num,i))
        primeFlag=False
        break
if primeFlag: print("{} is a prime number".format(num))