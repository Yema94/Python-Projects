# CRUD operations : Create, Read, Update, Delete

# step 1. Connecting to mysql database
# step 2. update an employee salary in employee table


import mysql.connector

def update(salary, id):
    str = "UPDATE emp SET salary='%d' WHERE id='%d'"
    args = (salary, id)
    cursor = conn.cursor()
    try:
        cursor.execute(str % args)
        conn.commit()
        print("Employee data updated")
    except:
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

# Connecting to mysql database
conn = mysql.connector.connect(host = "localhost", database = "mydb",
                               user = "root", password = "test1234")

# Checking if connection is being established or not
if conn.is_connected():
    print("Connected to mysql db")


id = int(input("Enter employee id:"))
salary = int(input("Enter the updated salary:"))

# invoking the update function and passing the parameters
update(salary, id)



