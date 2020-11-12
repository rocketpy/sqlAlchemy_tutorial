import sqlite3


conn = sqlite3.connect('customers.db')  # connecting to db

cur = conn.cursor()  # create a cursor

#  create a table
cur.execute("""CREATE TABLE customers(first_name text,
                                      second_name text,
                                      email text)
            """)

#  Datatypes: INTEGER, TEXT, NULL, BLOB, REAL

conn.commit()  # commit 

conn.close()  # close connection
