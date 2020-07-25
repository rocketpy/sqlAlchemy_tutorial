import sqlalchemy

# version
sqlalchemy.__version__ 


# connecting
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:', echo=True)
