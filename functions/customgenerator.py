# Generator is a function which creates a custom sequence
# usage of "yield"

def customgenerator(x, y):
    while x < y:
        if x % 2 == 0:
            # yields even numbers in the range
            yield x
        x += 1


result = customgenerator(2, 10)
print(list(result))
