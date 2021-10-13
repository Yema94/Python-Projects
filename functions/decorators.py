# Decor function takes a function type as a parameters and
# returns a inner function
# This inner function performs some action on the pass in function
# and returns the result

# defining decor function
def decor(fun):
    def inner():
        result = fun()
        return result * 2
    return inner


@decor
def num():
    return int(input())


resultfun = decor(num)
print(resultfun())

# print(num())
