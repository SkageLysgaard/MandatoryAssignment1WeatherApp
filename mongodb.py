import pymongo
from pymongo import MongoClient 

cluster = MongoClient("lim inn url her")
database = cluster["cluster"]
collection = database["collection"]

wheater_info = {"informasjonen fra station"}

wheater_info_update = collection.update_one({"informasjonen som skal inn i databasen"})