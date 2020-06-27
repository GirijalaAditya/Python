import cx_Oracle as cxo

con = cxo.connect("system/durga@192.168.1.9:1521/xe")
cursor = con.cursor()
while True:
    eno = int(input("Employee Number    : "))
    ename = input("Employee Name    : ")
    esal = float(input("Employee Salary   : "))
    eaddr = input("Employee Address   : ")
    cursor.execute("insert into emp1 values({emp_No},'{emp_Name}',{emp_Sal},'{emp_Addr}')".format(emp_No=eno,emp_Name=ename,emp_Sal=esal,emp_Addr=eaddr))
    con.commit()
    print("Employee",eno,"Inserted Successfully")
    option = input("Onemore Employee [yes/no]?   : ")
    if option == "yes":
        continue
    else:
        break


    

