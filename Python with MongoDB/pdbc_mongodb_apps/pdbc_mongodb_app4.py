import pymongo

client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
db = client['durgadb']
collection = db['emp1']
result = collection.find({"ESAL":{"$lt":10000}})
for document in result:
    print(document)

client.close()


