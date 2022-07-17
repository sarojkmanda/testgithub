import pymongo
client = pymongo.MongoClient("mongodb+srv://ineuron1:Dsaroj1808@cluster0.5csfl.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d= {
    "name":"saroj",
    "email": "saroj@gmail.com",
    "surname" :"kumar"
}
db1 = client['mongotest']
coll =db1['test']
coll.insert_one(d)