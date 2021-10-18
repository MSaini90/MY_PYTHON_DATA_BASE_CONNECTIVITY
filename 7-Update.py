import mysql.connector  
mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = 'db1')
cur = mydb.cursor()
s = "update book set price = price+90"
cur.execute(s)
mydb.commit()