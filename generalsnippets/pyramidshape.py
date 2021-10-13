# printing astericks/stars in pyramid shape
n = int(input("Enter a number: "))

# one way of doing it
"""for i in range(1, n+1):
    print(" "*(n-i), end = "")
    print("* "*i)"""

# another way of doing it
for i in range(1, n+1):
    print(" " * (n - i), end="")
    for j in range(1, i+1):
        print("* ", end = "")
    print()

