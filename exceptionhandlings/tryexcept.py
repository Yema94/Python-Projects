# Implementing
# Exception Handing : "try, except, else, finally"
# Logging and
# Assertions

import logging

logging.basicConfig(filename="debugging.log", level=logging.DEBUG)
logging.basicConfig(filename="errors.log", level=logging.ERROR)


try:
    f = open("myfile", "w")
    a, b = [int(x) for x in input("Enter two numbers: ").split()]
    logging.info("Division in progess")
    # assert b!=0
    c = a/b
    logging.info("Division finished")
    f.write("Writing {} into myfile".format(c))
    logging.info("Result saved into the file")
except AssertionError:
    print("second value should be non-zero")
except ZeroDivisionError:
    print("Division by zero is not allowed")
    print("Please enter a non zero number")
    logging.error("Division by zero")
else:
    print("You have entered a non-zero number")
finally:
    f.close()
    print("File closed")

print("Code after the exception")
