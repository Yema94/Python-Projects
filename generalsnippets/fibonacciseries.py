# fibonacci series using generators
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


c = fib()
print(list(c))

for i in c:
    if i > 20 and i < 100:
        continue
    elif i > 200:
        break
    print(i)