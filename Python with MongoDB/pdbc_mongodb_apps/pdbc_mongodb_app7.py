import pymongo

client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
db = client['durgadb']
collection = db['emp1']
collection.delete_one({"ENO":333})
print("Emploee Deleted Successfully")
client.close()


