#!/usr/bin/python
import subprocess
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","qwerty123")

# prepare a cursor object using cursor() method
cursor = db.cursor()

#execute the shell script
subprocess.call(['./test.sh'])
f=open("flow.txt")
for line in f:
        r=line.split(",")
        print r
        l=[]
        for a in r:
                k= str(a)
                p=k.split("=")
                l.append(p[1])
        print l	
	#print k,cookie # duration table n_packets n_bytes idle_age priority in_port dl_dst actions

# Open database connection
#db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

# prepare a cursor object using cursor() method
#cursor = db.cursor()

# execute SQL query using execute() method.
#sql = """CREATE TABLE EMPLOYEE (
         #FIRST_NAME  CHAR(20) NOT NULL,
         #LAST_NAME  CHAR(20),
         #AGE INT,  
         #SEX CHAR(1),
         #INCOME FLOAT )"""
#cursor.execute(sql)


# Fetch a single row using fetchone() method.
#data = cursor.fetchone()

#print "Database version : %s " % data

# disconnect from server
db.close()

