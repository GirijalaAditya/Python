import pymongo

client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
db = client['durgadb']
collection = db['emp1']

documentsList = []
while True:
    eno = int(input("Employee Number    : "))
    ename = input("Employee Name   : ")
    esal = float(input("Employee Salary   : "))
    eaddr = input("Employee Address  : ")
    document = {'ENO':eno, 'ENAME':ename, 'ESAL':esal, 'EADDR':eaddr}
    documentsList.append(document)
    option = input("Onemore Employee[yes/no]?   : ")
    if option == "yes":
        continue
    else:
        break

collection.insert_many(documentsList)
print("Employees Inserted Successfully")

client.close()

    


    

