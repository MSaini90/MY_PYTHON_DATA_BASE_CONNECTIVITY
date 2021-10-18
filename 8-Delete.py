import mysql.connector  
mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = 'db1')
cur = mydb.cursor()
s ="Delete from book where title ='php'"
cur.execute(s)
mydb.commit()