# lambda function syntax

# squaring the elements of a list
f = lambda x: [i**2 for i in x]
print(f([2, 3]))

# sum of two numbers
g = lambda x, y: x+y
print(g(2, 3))

# sum of multiple numbers
h = lambda *args: sum(list(args))
print(h(2, 3, 4, 5))

# return even or odd
j = lambda *num: "Even" if num % 2 == 0 else "Odd"
print(j(2))
