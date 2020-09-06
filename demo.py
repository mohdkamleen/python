#!C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\python.exe 
print("Content-Type: text/html\r\n\r\n")
import mysql.connector  
import cgi

form = cgi.FieldStorage()
name = form["name"].value
email = form["email"].value
password = form["password"].value

db = mysql.connector.connect(host='localhost', user='root', password='', database="jangosql") 
cr = db.cursor() 

     
cr.execute("INSERT INTO web_contact (username, password) VALUES (%s,%s)", (name, email))

db.commit()


cr.execute("select * from web_contact")
 
print(db)