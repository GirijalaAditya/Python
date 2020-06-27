import pymongo

client = pymongo.MongoClient()

db = client['durgadb']

empCollection = db.emp1

empCollection.insert_one({'ENO':111,'ENAME':"AAA",'ESAL':5000,'EADDR':"Hyd"})

print("Employee Inserted Successfully")

client.close()




