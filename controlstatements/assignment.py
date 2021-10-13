# Loops assignment

num = int(input("Please enter a number"))
for i in range(num):
    if i< 100:
        if i%10==0 : continue
        print(i)
    else : break