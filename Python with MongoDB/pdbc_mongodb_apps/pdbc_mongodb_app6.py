import pymongo

client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
db = client['durgadb']
collection = db['emp1']
collection.update_many({"ESAL":{"$lt":10000}},{"$inc":{"ESAL":500}})
print("Employees Updated Successfully")
client.close()

