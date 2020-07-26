import os
import sqlalchemy
from sqlalchemy import MetaData, Table, Column, String, Integer


# version
sqlalchemy.__version__ 


# connecting
from sqlalchemy import create_engine

engine = create_engine("sqlite:///some.db")
# engine = create_engine('sqlite:///:memory:', echo=True)

# creating a table
metadata = MetaData()
user_table = Table('user', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('username', String(50)),
                   Column('fullname', String(50))
                   )

# or 
if os.path.exists("some.db"):
    os.remove("some.db")
new_table = create_engine("sqlite:///some.db")
new_table.execute("""
    create table employee (
        emp_id integer primary key,
        emp_name varchar
    )
""")

# add new row
new_table.execute("""insert into employee(emp_name) values ('jack')""")


# execute
result = engine.execute("select emp_id, emp_name from " 
                        "employee where emp_id=:emp_id",
                        emp_id=3)
# query same like
# select emp_id, emp_name from employee where emp_id=3;
