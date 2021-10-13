'''# List Comprehensions
# I = [expression for item in iterable if condition]
# if condition is optional

# list of even numbers in a given range
# using list comprehensions
evenNumbers = [x for x in range(int(input("Enter a num : "))) if x % 2 == 0]
print(evenNumbers)'''


'''
# product of elements in two lists
# using list comprehension
list1 = [1, 2, 3]
list2 = [4, 5, 6]

"""
for i in range(len(list1)):
    product.append(list1[i] * list2[i])"""

product = [list1[i] * list2[i] for i in range(len(list1))]

print(product)'''


# Common elements of two lists

list1 = [2, 3, 4, 5, 6, 7, 8]
list2 = [3, 4, 7, 8, 9]
'''
commonElements = []
for x in list1:
    if x in list2:
        commonElements.append(x)'''
commonElements = [x for x in list1 if x in list2]
print(commonElements)
