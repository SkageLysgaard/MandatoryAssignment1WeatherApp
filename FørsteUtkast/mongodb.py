import pymongo
from pymongo import MongoClient 

cluster = MongoClient("mongodb://adminGroven:<12345678!>@weatherstoragedb-shard-00-00.8q1zq.mongodb.net:27017,weatherstoragedb-shard-00-01.8q1zq.mongodb.net:27017,weatherstoragedb-shard-00-02.8q1zq.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-ubvlc6-shard-0&authSource=admin&retryWrites=true&w=majority")
database = cluster["cluster"]
collection = database["collection"]

wheater_info = {"informasjonen fra station"}
post1 = {"_id":5, "name" : "bill"}
wheater_info_update = collection.update_one({post1})
