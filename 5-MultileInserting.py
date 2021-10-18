import mysql.connector  
mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = 'db1')

#@@@@@@@@@@ Inserting Data in table @@@@@@@@@@@ 

cur = mydb.cursor()
s = "Insert into book(bookid,title,price) values(%s,%s,%s)"
books = [(2,'python2',348),(3,'php',737)]
cur.executemany(s,books)
mydb.commit() # we have to find about this