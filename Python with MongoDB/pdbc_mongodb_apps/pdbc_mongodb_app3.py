import pymongo

client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
db = client['durgadb']
collection = db['emp1']
result = collection.find_one({"ENO":111})
print(result)
client.close()

