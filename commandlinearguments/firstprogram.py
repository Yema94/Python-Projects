# First Program Using "Command Line Arguments" and
# Product of given inputs through "CLA"

import sys
inputsList = [int(x) for x in sys.argv[1:]]
product = 1
for i in inputsList: product *=i
print("product is {}".format(product))