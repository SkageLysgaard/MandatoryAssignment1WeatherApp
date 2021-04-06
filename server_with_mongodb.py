from socket import create_server
from time import sleep
from station import StationSimulator
import pymongo
from pymongo import MongoClient 

server = create_server(("localhost", 5550))
print("host")
print("Waiting for ant incomming connections...")
conn, addr = server.accept()
location = conn.recv(1024).decode()
print(addr, "Has connected to the server", location)
cluster = MongoClient("mongodb://adminGroven:<12345678!>@weatherstoragedb-shard-00-00.8q1zq.mongodb.net:27017,weatherstoragedb-shard-00-01.8q1zq.mongodb.net:27017,weatherstoragedb-shard-00-02.8q1zq.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-ubvlc6-shard-0&authSource=admin&retryWrites=true&w=majority"))
database = cluster["cluster"]
collection = database["collection"]
 


if __name__ == "__main__":
    bergen_station = StationSimulator(simulation_interval=1)
    bergen_station.turn_on()
    
    for _ in range(72):
        # Sleep for 1 second to wait for new weather data
        # to be simulated
        sleep(1)
        # Read new weather data and append it to the
        # corresponding list
        post = {"location":bergen_station.location,"month":bergen_station.month, "temperature":bergen_station.temperature, "rain":bergen_station.rain}
        collection.insert_one(post)
    bergen_station.shut_down()
else:
    print("Sorry, i didn't get that")

'''
filename = location
file = open(filename , "rb")
file_data = file.read(1024)
conn.send(file_data)
print("Data has been sendt successfully!")
'''