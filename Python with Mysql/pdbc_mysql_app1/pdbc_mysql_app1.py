import mysql.connector as mysql

con = mysql.connect(host="localhost",port=3306,user="root",password="root",database="durgadb")
cursor = con.cursor()
tname = input("Table Name : ")
cursor.execute("create table "+tname+"(ENO int(3) primary key, ENAME char(10), ESAL float(5), EADDR char(10))")
con.commit()
print("Table",tname,"Created Successfully")
cursor.close
cursor.close()
con.close()






