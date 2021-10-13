# CRUD operations : Create, Read, Update, Delete
# 1. connecting to mysql database
# 2. deleting a record from the emp table based on the id

import mysql.connector

def delete(id):

    str = "delete from emp where id = '%d'"
    args = (id)
    try:
        cursor.execute(str % args)
        conn.commit()
        print("Employee deleted")
    except:
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

conn = mysql.connector.connect(host="localhost", database = "mydb",
                               user = "root" , password = "test1234")

if conn.is_connected():
    print("Connected to mysql db")
cursor = conn.cursor()

empId = int(input("Enter emp id: "))


delete(empId)