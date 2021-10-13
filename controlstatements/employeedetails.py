# Handle Employee Details

employeeCount = int(input("Enter the number of employeees : "))
employeeDetails = {}
for i in range(employeeCount):
    employeeName = input("Enter employee name: ").lower().strip()
    employeeDetails[employeeName] = float(input("Enter the salary : "))
while True:
    checkEmployee = input("Enter employee name to know his salary : ").lower().strip()
    if checkEmployee in employeeDetails.keys():
        print("{}'s salary is {}".format(checkEmployee, employeeDetails[checkEmployee]))
    else: print("Employee does not exist!")
    while True:
        choice = input("To know the details of another employee enter 'YES' otherwise enter 'NO' : ").lower()
        if choice == 'no': break
        #elif choice == 'yes' : break
        else: print("please enter either 'yes' or 'no' only!\n" )

    if choice == 'no' : break
