def f1(f):
    print('funtion 1', )


def f2(f):
    print('funtion 2', f)


def f3():
    x=10
    print('funtion 3')
    return x

f1(f2(f3()))