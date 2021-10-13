from os import path
import sys

# to check if the file actually exists
if path.isfile("credentials.txt"):
    f = open("credentials.txt", "r")
else:
    print("File does not exist")
    sys.exit()

s = f.readlines()
print(s, type(s ), len(s))
f.close()