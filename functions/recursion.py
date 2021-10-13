# Implementing recursion function concept and
# calculating factorial program

def factorial(n):
    # condition to stop the recursion(very important)
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(5))
