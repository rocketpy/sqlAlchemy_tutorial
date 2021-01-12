#  pip install mysql-connector

import mysql.connector


db_connection = mysql.connector.connect(host="hostname",
  	                                    user="username",
  	                                    passwd="password"
                                       )
