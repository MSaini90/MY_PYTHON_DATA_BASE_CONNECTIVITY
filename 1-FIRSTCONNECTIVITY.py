
           # @@@@@ Command for making connection  @@@@@@@@
import mysql.connector  
mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "")
print(mydb.connection_id)

