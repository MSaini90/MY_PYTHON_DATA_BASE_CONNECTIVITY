# @@@@@ Command for making connection  @@@@@@@@
import mysql.connector  
mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = 'db1')

#@@@@@@@@@@ Create table @@@@@@@@@@@ 
cur = mydb.cursor()
s = "create table book2(bookid integer(4) , title varchar(20) , price float(5,4))"
cur.execute(s)
