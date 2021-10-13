def xor(x,y):
    return x^y

def reduce(func, seq):
    x = seq[0]
    for s in seq[1:]:
        x = func(x, s)
        yield x

for a in reduce(xor, [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]):
    print(a)