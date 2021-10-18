import mysql.connector  
mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = 'db1')
cur = mydb.cursor()
s = "Select * from book"
cur.execute(s)
result = cur.fetchall()
for rec in result:
	print(rec)