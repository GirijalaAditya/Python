import mysql.connector as mysql

con = mysql.connect(host="localhost", port=3306, user="root", password="root", database="durgadb")
cursor = con.cursor()
cursor.execute("drop table emp1")
con.commit()
print("Table emp1 dropped Successfully")
cursor.close()
con.close()



