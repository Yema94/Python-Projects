# Input is a function - input()

#by default the given input is considered as a String.
firstInput = input("Enter a number : ")
print("First input is {} and its type is {}".format(firstInput,type(firstInput)))

#type casting.. eg: int(), str(), float(), bool()
secondInput = int(input("Enter another number : "))
print("Second input is {} and its type is {}".format(secondInput, type(secondInput)))

#Multiple inputs

#1st way
a = input("Enter 3 numbers : ").split()
print(a)

for i in range(len(a)): a[i] = int(a[i])
print(a)

#2nd way
b = [int(x) for x in input("Enter 3 numbers using comma"
                           "as a separator : ").split(',')]
print(b)