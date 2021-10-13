def digital_root(num):
    if len(str(num))==1:
        return num
    else:
        return digital_root(eval('+'.join(str(num))))


print(digital_root(15))
print(digital_root(129))