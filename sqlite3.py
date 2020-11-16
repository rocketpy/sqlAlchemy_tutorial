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

#  get data by ID
cur.execute("SELECT rowid, * FROM customers")
items = cur.fetchall()

for item in items:
    print(item)  # result will contain ID every row
   
# using WHERE
cur.execute("SELECT * FROM customers WHERE age >= 35")
#  or
cur.execute("SELECT * FROM customers WHERE name = 'Jack' ")
#  or
cur.execute("SELECT * FROM customers WHERE name LIKE 'J%' ")
#  or
cur.execute("SELECT * FROM customers WHERE email LIKE '%gmail.com' ")
    
conn.close()  # close connection

# Updating a data 
cur.execute("""UPDATE customers SET name = 'John' WHERE surname = 'Grey' """)

# Updating a data for first row
cur.execute("""UPDATE customers SET name = 'John' WHERE rowid = 1 """)

cur.commit()
conn.close()

# Delete some row
cur.execute("DELETE FROM customers WHERE rowid = 5 ")

#  ORDER BY:  ASC and DESC
cur.execute("SELECT * FROM customers ORDER BY rowid DESC")
#  or
cur.execute("SELECT * FROM customers ORDER BY name")  # alphabet


#  AND / OR
cur.execute("SELECT * FROM customers WHERE age == 25 AND name == 'J%' ")
