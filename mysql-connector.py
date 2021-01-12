#  pip install mysql-connector

import mysql.connector


db_connection = mysql.connector.connect(host="hostname",
  	                                    user="username",
  	                                    passwd="password"
                                       )
print(db_connection)

# Create new database  
# CREATE DATABASE "database_name"

import mysql.connector


db_connection = mysql.connector.connect(host= "localhost",
                                        user= "root",
                                        passwd= "root"
                                       )

# creating database_cursor to perform SQL operation
db_cursor = db_connection.cursor()

# executing cursor with execute method and pass SQL query
db_cursor.execute("CREATE DATABASE my_first_db")

# get list of all databases
db_cursor.execute("SHOW DATABASES")

# print all databases
for db in db_cursor:
	print(db)
	
# create a simple table "student" with two columns	
# CREATE  TABLE student (id INT, name VARCHAR(255))

import mysql.connector


db_connection = mysql.connector.connect(host="localhost",
                                        user="root",
                                        passwd="root",
                                        database="my_first_db"
				       )

db_cursor = db_connection.cursor()

# creating database table as student
db_cursor.execute("CREATE TABLE student (id INT, name VARCHAR(255))")

# for get a table
db_cursor.execute("SHOW TABLES")
for table in db_cursor:
	print(table)
	
#  Create a Table with Primary Key
#  CREATE TABLE employee(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), salary INT(6))

import mysql.connector
	
	
db_connection = mysql.connector.connect(host="localhost",
                                        user="root",
                                        passwd="root",
                                        database="my_first_db"
				       )
db_cursor = db_connection.cursor()

# creating database table with primary key
db_cursor.execute("CREATE TABLE employee(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), salary INT(6))")

# get database table
db_cursor.execute("SHOW TABLES")

for table in db_cursor:
	print(table)	

	
# using ALTER table
#  ALTER TABLE student MODIFY id INT PRIMARY KEY

import mysql.connector
	
	
db_connection = mysql.connector.connect(host="localhost",
                                        user="root",
                                        passwd="root",
                                        database="my_first_db"
				       )

db_cursor = db_connection.cursor()

# modify existing column id
db_cursor.execute("ALTER TABLE student MODIFY id INT PRIMARY KEY")


#  Insert operation
#  INSERT INTO student (id, name) VALUES (01, "John")
#  INSERT INTO employee (id, name, salary) VALUES(01, "John", 10000)

import mysql.connector
	
	
db_connection = mysql.connector.connect(host="localhost",
                                        user="root",
                                        passwd="root",
                                        database="my_first_db"
				       )

db_cursor = db_connection.cursor()

student_sql_query = "INSERT INTO student(id,name) VALUES(01, 'John')"
employee_sql_query = " INSERT INTO employee (id, name, salary) VALUES (01, 'John', 10000)"

# execute cursor and pass query
db_cursor.execute(student_sql_query)

# execute cursor and pass query
db_cursor.execute(employee_sql_query)
db_connection.commit()

print(db_cursor.rowcount, "Record Inserted")

