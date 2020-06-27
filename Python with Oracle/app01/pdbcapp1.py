import cx_Oracle as cxo

con = cxo.connect("system/durga@192.168.1.9:1521/xe")
cursor = con.cursor()
tname = input("Enter Table Name : ")
cursor.execute("create table "+tname+"(ENO number(3) primary key, ENAME varchar2(10), ESAL float(5), EADDR varchar2(10))")
con.commit()
print("Table",tname,"Created Successfully")
cursor.close()
con.close()


