# While loop:

"""
marksList = [float(mark) for mark in input("enter 3 numbers using comma: " ).split(',')]
while marksList:
    print(marksList.pop(1))
"""

# Even or Odd numbers between a and b using while loop
"""
a = int(input("Enter a number: "))
b = int(input("Enter another number : "))
while a<=b:
    if a%2==0 : print(a, "is an even number")
    a+=1
"""

#Multiplication table using while loop
"""
table = int(input("Which table you want brother ? "))
i = 1
while i<=10:
    print("{} * {} = {}".format(table, i, table*i))
    i+=1
"""


#**************************************************************************************************


#for loop:
"""is used to iterate over a element of a sequence
sequence types : string, list, tuple, set, range etc
"""

#display the alternate numbers between 50 and 70
"""
for i in range(50, 70, 2):
    print(i)
"""

#sum and product of a list using for list
"""
numbersList = [int(x) for x in input("Enter the numbers: ").split()]
print("Sum is {}".format(sum(numbersList)))
prod = 1
for number in numbersList:
   prod*=number
print(prod)
"""

#factorial calculator
"""
number = int(input("Calculate the factorial of "))
fact = 1
for i in range(number + 1): fact *= i
print(fact,"\n")
"""

#multipilcation table using for loop
"""
number = int(input("Which table you want brother ? "))
for i in range(1,11): print("%i * %i = %i" %(number, i, number*i))
"""

# Break statement usage
"""
number = int(input("Which table you want brother ? "))
for i in range(1,15):
    print("%i * %i = %i" %(number, i, number*i))
    if i == 10: break
"""

# continue statement usage using for loop
"""
for i in range(1, 20):
    if i%3 == 0 : continue
    print("{} is not the multiple of 3".format(i))
"""

# continue statement usage using while loop
"""
x=0
while x<=20:
    x += 1
    if x%3==0 : continue
    print("{} is not the multiple of 3".format(x))
"""

# Check and Assert the number.. assert is a type of exceptional handling
"""
num = int(input("Enter a number > 10 : "))
assert num > 10, "Enter correct number"
print("U entered {}".format(num))
"""

# Duplicates removal from List
lst = list(set(eval(input("Enter a list of elements in square braces"))))
print(lst)