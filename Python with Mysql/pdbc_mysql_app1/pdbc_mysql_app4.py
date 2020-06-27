import mysql.connector as mysql

con = mysql.connect(host="localhost", port=3306, user="root", password="root",database="durgadb")
cursor = con.cursor()
cursor.execute("delete from emp1 where ESAL < 10000")
con.commit()
print("Employees Deleted Successfully")
cursor.close()
con.close()


