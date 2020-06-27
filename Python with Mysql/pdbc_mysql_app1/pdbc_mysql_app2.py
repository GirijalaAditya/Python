import mysql.connector as mysql

con = mysql.connect(host="localhost",port=3306,user="root",password="root",database="durgadb")
cursor = con.cursor()
while True:
    eno = int(input("Employee Number   : "))
    ename = input("Employee Name   : ")
    esal = float(input("Employee Salary   : "))
    eaddr = input("Employee Address   : ")

    cursor.execute("insert into emp1 values(%i,'%s',%f,'%s')"%(eno,ename,esal,eaddr))
    con.commit()
    print("Employee",eno,"Inserted Successfully")
    option = input("Onemore Employee[yes/no]?  : ")
    if option == "yes":
        continue
    else:
        break
cursor.close()
con.close()



