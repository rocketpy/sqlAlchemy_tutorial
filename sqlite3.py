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

#  add new one customer
cur.execute("INSERT INTO customers VALUES ('John', 'Doe', 'jdoe@gmail.com')")   # insert data to table 'customers'

#  adding a many customers
customers_list = [('John', 'Doe', 'jdoe@gmail.com'),
                 ('Jack', 'Woe', 'j_woe@gmail.com'),
                 ('Jill', 'Boe', 'jill_boegmail.com')
                 ]
cur.executemany("INSERT INTO customers VALUES (?,?,?)", customers_list) 

conn.commit()  # commit 

conn.close()  # close connection
