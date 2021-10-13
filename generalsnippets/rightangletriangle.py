# printing in right angle triangle shape

def asterick():
    return "* "


def print_right_angle_triangle_shape(n):
    for i in range(1, n + 1):
        # j represents colomns
        for j in range(1, i + 1):
            print(asterick(), end="")
        print()


num = int(input("Enter a number:"))
print_right_angle_triangle_shape(num)

# one way printing stars/astericks in right angle triangle shape
"""for i in range(1,n+1):
    print("* "*i)"""

# another way of doing it if rows and columns are now equal
# i represents rows
"""for i in range(1, n + 1):
    # j represents colomns
    for j in range(1, i + 1):
        print(asterick(), end="")
    print()"""
