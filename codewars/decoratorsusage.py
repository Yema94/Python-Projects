from debugging import debug

"""def add(x,y):
    return x+y
add = debug(add)"""

@debug
def add(x,y):
    return x+y

print(add(2,3))