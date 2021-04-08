from socket import socket, AF_INET,SOCK_STREAM, SOCK_DGRAM, SOL_SOCKET, SO_REUSEADDR
import threading
import csv
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb://adminGroven:12345678!@weatherstoragedb-shard-00-00.8q1zq.mongodb.net:27017,weatherstoragedb-shard-00-01.8q1zq.mongodb.net:27017,weatherstoragedb-shard-00-02.8q1zq.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-ubvlc6-shard-0&authSource=admin&retryWrites=true&w=majority")
database = cluster["WeatherStorageDB"]
collection = database["location"]


socketTCP = socket(AF_INET,SOCK_STREAM)
socketTCP.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
socketUDPBergen = socket(AF_INET,SOCK_DGRAM)
socketUDPBergen.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
socketUDPTromso = socket(AF_INET,SOCK_DGRAM)
socketUDPTromso.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
socketUDPOslo = socket(AF_INET,SOCK_DGRAM)
socketUDPOslo.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)



socketTCP.bind(("localhost", 5558))
socketUDPBergen.bind(("localhost", 5560))
socketUDPTromso.bind(("localhost", 5561))
socketUDPOslo.bind(("localhost", 5562))




def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connected = True
    while connected:
        msg_length = conn.recv(64)
    conn.close()

def receive_information_UDP_Bergen():
    while True:
        weatherData , UDP_adress = socketUDPBergen.recvfrom(2048)
        decoded = weatherData.decode()
        print("Recieved" + decoded)
        with open("DATABERGEN.txt", "a") as data:
            #csv.writer(data).writerow(decoded)
            data.write(decoded + "\n")
def receive_information_UDP_Tromso():
    while True:
        weatherData , UDP_adress = socketUDPTromso.recvfrom(2048)
        decoded = weatherData.decode()
        print("Recieved" + decoded)
        with open("DATATROMSO.txt", "a") as data:
            #csv.writer(data).writerow(decoded)
            data.write(decoded + "\n")
def receive_information_UDP_Oslo():
    while True:
        weatherData , UDP_adress = socketUDPOslo.recvfrom(2048)
        decoded = weatherData.decode()
        print("Recieved" + decoded)
        with open("DATAOSLO.txt", "a") as data:
            #csv.writer(data).writerow(decoded)
            data.write(decoded + "\n")

def receive_information_client():
    socketTCP.listen()
    print("[LISTENING] The server is listening on ...")
    conn, TCP_addr = socketTCP.accept()
    cities = ['OSLO', 'BERGEN', 'TROMSO']
    while True:
        data = conn.recv(1024).decode()
        print(f'Received message from {TCP_addr}, message: {data}')
        conn.send(data.encode())
        if(data in cities):
            textfile = 'DATA' + str(data) + '.txt'
            with open(textfile) as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    post = {"_id":0, "location":row[0].location,"month":row[1], "temperature":row[2], "rain":row[4]}
                    collection.update_one({post})
                    encoded = f'{row[0]},{row[1]},{row[2]},{row[3]} \n'.encode()
                    print(encoded.decode())
                    conn.send(encoded)
        if(data == 'DISCONNECT'):
            conn.close()

#Definerer threading for hver metode
TCP = threading.Thread(target=receive_information_client)
UDP_B = threading.Thread(target=receive_information_UDP_Bergen)
UDP_T = threading.Thread(target=receive_information_UDP_Tromso)
UDP_O = threading.Thread(target=receive_information_UDP_Oslo)

#Starter Threading
TCP.start()
UDP_B.start()
UDP_T.start()
UDP_O.start()


