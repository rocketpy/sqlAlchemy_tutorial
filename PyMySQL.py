# PyPi: https://pypi.org/project/PyMySQL/
# Docs: https://pymysql.readthedocs.io/en/latest/user/installation.html
#  pip install PyMySQL

import pymysql
import pymysql.cursors


# create a table
CREATE TABLE `users` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `email` varchar(255) COLLATE utf8_bin NOT NULL,
    `password` varchar(255) COLLATE utf8_bin NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
AUTO_INCREMENT=1 ;

# CRUD
# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='user',
                             password='passwd',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()

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
        
        
# get data by cursor dict 
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
        
        
# get column names
con = pymysql.connect('localhost', 'user17', 
    's$cret', 'testdb')
 
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM cities")
    rows = cur.fetchall()
    desc = cur.description
    print("{0:>3} {1:>10}".format(desc[0][0], desc[1][0]))
    for row in rows:    
        print("{0:3} {1:>10}".format(row[0], row[2]))
