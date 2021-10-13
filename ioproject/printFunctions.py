#print function is "print()"
""" \t - tab, \n - new line
    sep(' ')
    place holders or special string formattings
    eg: %s , %f, %i - %(element)
    eg: {} - .format(element)"""

print("\tHello! \nPlease check the following")

a = [10,19,18.2, "Kilo"]
b = [34.32, 44, "Float", "Weight"]
for i,j,k,l in a,b: print(i,j,k,l, sep=' \t:\t ')

name = input("Enter you name here : ")
print("name of the person is",name)
#Place Holders or Special Formating strings
print("name of the person is %s" %(name)) # %.2f - restricts to 2 decimal point.. eg: 9.55
print("name of the person is {}".format(name)) # cannot restrict any decimal point