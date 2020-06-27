import mysql.connector as mysql

con = mysql.connect(host="localhost",port=3306, user="root", password="root",database="durgadb")
cursor = con.cursor()
cursor.execute("update emp1 set ESAL = ESAL + 500 where ESAL < 10000")
con.commit()
print("Employee Updated Successfully")
cursor.close()
con.close()


