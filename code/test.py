import psycopg2
import os
from subprocess import Popen, PIPE

def getdsn(db = 'adama_qa', user = 'postgres', host = '172.17.0.3'):
    if user == None:
        import os, pwd
        user = pwd.getpwuid(os.getuid())[0]
    if db == None:
        db = user
    dsn = 'dbname=%s user=%s' % (db, user)
    
    if host != None:
        dsn += ' host=' + host
    return dsn

dsn = getdsn()
print "Connecting to %s" % dsn
dbh = psycopg2.connect(dsn)
print "Connection successful."

cur = dbh.cursor()
#cur.execute("""CREATE TABLE myTable(mynum integer UNIQUE,mystring  varchar(30))""")
#cur.execute("INSERT INTO myTable VALUES (6, 'Six')")
#cur.execute("INSERT INTO myTable VALUES (1, 'One')")
cur.execute("SELECT * FROM myTable")
rows = cur.fetchall()

for row in rows:
    print row

dbh.commit()
dbh.close()