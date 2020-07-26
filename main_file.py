import sqlalchemy

# version
sqlalchemy.__version__ 


# connecting
from sqlalchemy import create_engine

engine = create_engine("sqlite:///some.db")
# engine = create_engine('sqlite:///:memory:', echo=True)

# execute
result = engine.execute("select emp_id, emp_name from " 
                        "employee where emp_id=:emp_id",
                        emp_id=3)
# query same like
# select emp_id, emp_name from employee where emp_id=3;
