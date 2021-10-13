def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

n = 3
# pyramid logic
for i in range(1, n+1):
    print(" "*(n-i), end = "")
    for j in range(1, i+1):
        for k in fib():
            if k > 20:
                break
        print("{} ".format(k), end = "")
    print()