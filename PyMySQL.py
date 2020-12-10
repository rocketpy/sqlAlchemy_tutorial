#  pip install PyMySQL

import pymysql
import pymysql.cursors


# fetchAll
con = pymysql.connect('localhost', 'user17', 
    'secret_password', 'testdb')
 
with con: 
    cur = con.cursor()
    cur.execute("SELECT * FROM cities")
 
    rows = cur.fetchall()
    # row = cur.fetchone()    
 
    for row in rows:
        print("{0} {1} {2}".format(row[0], row[1], row[2]))
        
        
# get column names by cursor dict 
con = pymysql.connect(host='localhost',
        user='user17',
        password='s$cret',
        db='mydb',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)
 
with con:
 
    cur = con.cursor()
    cur.execute("SELECT * FROM cities")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row["id"], row["name"])
