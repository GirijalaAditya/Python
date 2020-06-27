import cx_Oracle as cxo

con = cxo.connect("system/durga@192.168.1.9:1521/xe")
cursor = con.cursor()
cursor.execute("delete from emp1 where ESAL < 10000")
con.commit()
print("Employees Deleted Successfully")
cursor.close()
con.close()

