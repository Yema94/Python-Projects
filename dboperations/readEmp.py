# CRUD operations : Create, Read, Update, Delete
# reading/fetching the data from the database from within
# our python program
# 1. connecting the python to the mysql database
# 2. fetch the data one at a time or all at once

import mysql.connector

conn = mysql.connector.connect(host="localhost", database = "mydb",
                               user = "root", password = "test1234")

if conn.is_connected():
    print("Connected to mysql db")

# to do database operations we need cursor object
cursor = conn.cursor()

# now onwards use this cursor obj and execute whatever the sql
# statements we want
# using cursor to pass and execute the sql statements

# using execute method on the cursor obj to run the select statement/sql query
# records/data returned from the emp table is stored in cursor obj
# In other words : Cursor obj holds the data that comes back from select query
cursor.execute('select * from emp')

# fetching records one at a time from the cursor object
"""row = cursor.fetchone()
while row is not None:
    print(row)
    row = cursor.fetchone()"""

# fetching all the records at once
rows = cursor.fetchall()
print("Total number of records ", cursor.rowcount)
for row in rows:
    print(row)

cursor.close()
conn.close()