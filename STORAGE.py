from socket import socket, AF_INET,SOCK_STREAM, SOCK_DGRAM, SOL_SOCKET, SO_REUSEADDR
import threading
import csv
import pymongo
from pymongo import MongoClient
import json
from dotenv import load_dotenv
load_dotenv()
import os


username = "admin"
clusterName = "INFOBLIG"



client = MongoClient("mongodb+srv://adminGroven:12345678!@WeatherStorageDB.8q1zq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

database = client.Location
collection = database.location




#Oppretter sockets til hver av værestasjonene samt klienten 


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




#Lager metoder for å håndtere hver av socketsene ved hjelp av threading 

def receive_information_UDP_Bergen():
    while True:
        weatherData , _ = socketUDPBergen.recvfrom(2048)
        decoded = weatherData.decode()
        print("Recieved" + decoded)
        with open("DATABERGEN.csv", "a") as data:
            data.write(decoded + "\n")
def receive_information_UDP_Tromso():
    while True:
        weatherData , _ = socketUDPTromso.recvfrom(2048)
        decoded = weatherData.decode()
        print("Recieved" + decoded)
        with open("DATATROMSO.csv", "a") as data:
            decode = json.dumps(decoded)
            data.write(decode + "\n")
def receive_information_UDP_Oslo():
    while True:
        weatherData , _ = socketUDPOslo.recvfrom(2048)
        decoded = weatherData.decode()
        print("Recieved" + decoded)
        with open("DATAOSLO.csv", "a") as data:
            decode = json.dumps(decoded)
            data.write(decode + "\n")


def receive_information_client():
    socketTCP.listen()
    print("[LISTENING] The server is listening on ...")
    conn, TCP_addr = socketTCP.accept()
    cities = ['OSLO', 'BERGEN', 'TROMSO']
    DATA = [] 

    data = conn.recv(1024).decode()
    print(f'Received message from {TCP_addr}, message: {data}')
    if(data in cities): #Sjekker om input fra bruker er i cities 
        textfile = 'DATA' + str(data) + '.csv' #lager varabel som samsvarer med hvilken by bruker har valgt
        with open(textfile) as csv_file: 
            csv_reader = csv.reader(csv_file, delimiter = '\n')
            for row in csv_reader:
                DATA.append(row)
                obj = row[0]
                obje = json.loads(obj)
                collection.insert_one(obje) #sender dict til MongoDB database
            conn.send(str(DATA).encode()) #sender data fra værstasjonen til brukeren
    

#Definerer threading for hver metode
UDP_B = threading.Thread(target=receive_information_UDP_Bergen)
UDP_T = threading.Thread(target=receive_information_UDP_Tromso)
UDP_O = threading.Thread(target=receive_information_UDP_Oslo)
TCP = threading.Thread(target=receive_information_client)

#Starter Threading
UDP_B.start()
UDP_T.start()
UDP_O.start()
TCP.start()



