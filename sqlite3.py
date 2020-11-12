import sqlite3


conn = sqlite3.connect('customers.db')  # connecting to db

cur = conn.cursor()  # create a cursor

#  Datatypes: INTEGER, TEXT, NULL, BLOB, REAL

#  create a table
cur.execute("""CREATE TABLE customers(first_name text,
                                      second_name text,
                                      email text
                                      )          
           """)

cur.execute("INSERT INTO customers VALUES ('John', 'Doe', 'jdoe@gmail.com')")   # insert data to table 'customers'

conn.commit()  # commit 

conn.close()  # close connection
