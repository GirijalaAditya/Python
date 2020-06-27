import cx_Oracle as cxo

con = cxo.connect("system/durga@192.168.1.9:1521/xe")
cursor = con.cursor()
cursor.execute("drop table emp1")
con.commit()
print("Table emp1 Dropped Successfully")
cursor.close()
con.close()

