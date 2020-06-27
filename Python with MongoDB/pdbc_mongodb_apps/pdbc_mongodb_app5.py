import pymongo

client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
db = client['durgadb']
collection = db['emp1']
collection.update_one({"ENO":111},{"$inc":{"ESAL":500}})
print("Employee Updated Successfully")
client.close()
