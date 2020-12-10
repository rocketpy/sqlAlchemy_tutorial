#  pip install PyMySQL

import pymysql

# fetchAll
con = pymysql.connect('localhost', 'user17', 
    'secret_password', 'testdb')
 
with con: 
    cur = con.cursor()
    cur.execute("SELECT * FROM cities")
 
    rows = cur.fetchall()
 
    for row in rows:
        print("{0} {1} {2}".format(row[0], row[1], row[2]))
