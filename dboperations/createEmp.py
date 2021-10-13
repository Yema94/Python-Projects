# CRUD operations : Create, Read, Update, Delete
# performing create operation or insert a record into the employee table
# 1. Connect to the mysql database
# 2. insert a record into the employee table

import mysql.connector

# creating a conneciton to mysql database
conn = mysql.connector.connect(host='localhost', database = "mydb",
                               user = "root", password = "test1234")

# checking if the connection to mysql db is being establised or not
if conn.is_connected():
    print("Connected to mysql db")

# cursor obj, to do database operations
cursor = conn.cursor()

id = int(input("Enter employee id: "))
name = input("Enter employee name: ")
salary = int(input("Enter employee salary: "))

str = "insert into emp values('%d', '%s', '%d')"
args = (id, name, salary)
try:
    # using cursor here to execute the insert statement
    cursor.execute(str % args)

    # whenever we deal with DML statements, we should either commit
    # or rollback, which are generally used for Transaction management
    # Insert, Update and delete statements are called DML statements

    conn.commit()
    print("Employee added!")
except:
    conn.rollback()
finally:
    cursor.close()
    conn.close()

