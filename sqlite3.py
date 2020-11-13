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
conn.commit()  # commit 

#  adding a many customers
customers_list = [('John', 'Doe', 'jdoe@gmail.com'),
                 ('Jack', 'Woe', 'j_woe@gmail.com'),
                 ('Jill', 'Boe', 'jill_boegmail.com')
                 ]
cur.executemany("INSERT INTO customers VALUES (?,?,?)", customers_list) 
conn.commit()  # commit 

# fetch (get) data from table
cur.execute("SELECT * FROM customers")
cur.fetchone()  # return first row from table
cur.fetchone()[0]  # return first cell from this row 

cur.fetchmany(5)

cur.fetchall()
# print(cur.fetchall())  # will return a list with data

items = cur.fetchall()
print(items[0])  # return first row

conn.close()  # close connection
