import mysql.connector  
mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = 'db1')

#@@@@@@@@@@ Inserting Data in table @@@@@@@@@@@ 

cur = mydb.cursor()
s = "Insert into book(bookid,title,price) values(%s,%s,%s)"
b1 = (1,'python3',848)
cur.execute(s,b1)
mydb.commit() # we have to find about this