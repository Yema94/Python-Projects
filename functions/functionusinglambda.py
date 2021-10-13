from functools import reduce

# filter the even numbers of a list
# using lambda function in the filter function
testList = [2, 3, 44, 54, 55, 4, 55]
evenNumbers = list(filter(lambda x: x % 2 == 0, testList))
print(evenNumbers)

# Double each value of a list
# using lambda function in a map function
testList = list(map(lambda x: x * 2, testList))
print(testList)

# sum of all elements in a list
# using lambda function in a reduce function
result = reduce(lambda x, y: x + y, testList)
print(result)
