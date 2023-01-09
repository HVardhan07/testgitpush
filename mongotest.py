import pymongo

client = pymongo.MongoClient("mongodb+srv://HVMongo:Mongo123Mongo@cluster0.mrhqdi5.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d={
    "name": "harsha",
    "email": "harsha@abc.com",
    "surname": "pendyala"
}

db1= client['mongotest']
coll=db1['test']
coll.insert_one(d)