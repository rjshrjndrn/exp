#!/usr/bin/env python
#Set up MySQL connection
import MySQLdb
db = MySQLdb.connect(host="localhost",user='python',passwd='python',db='python')
cursor=db.cursor()
#insert row in to table;
cursor.execute("INSERT INTO users (firstname) VALUES ('Keenan')")
db.commit()
