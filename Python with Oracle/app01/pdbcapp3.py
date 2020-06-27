import cx_Oracle as cxo

con = cxo.connect("system/durga@192.168.1.9:1521/xe")
cursor = con.cursor()
cursor.execute("update emp1 set ESAL = ESAL + 500 where ESAL < 10000")
con.commit()
print("Employee Updated Successfully")
cursor.close()
con.close()

