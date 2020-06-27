import cx_Oracle as cxo

con = cxo.connect("system/durga@192.168.1.9:1521/xe")
cursor = con.cursor()
cursor.execute("select * from emp1")
data = cursor.fetchmany(3)
print(data)
cursor.close()
con.close()


