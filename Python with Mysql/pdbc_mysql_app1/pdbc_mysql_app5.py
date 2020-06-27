import mysql.connector as mysql

con = mysql.connect(host="localhost", port=3306, user="root", password="root", database="durgadb")
cursor = con.cursor()
cursor.execute("select * from emp1")
data = cursor.fetchone()
print(data)

cursor.close()
con.close()

    
