from socket import socket, AF_INET,SOCK_STREAM, SOCK_DGRAM, SOL_SOCKET, SO_REUSEADDR
from threading import Thread
import csv

socketUDP = socket(AF_INET,SOCK_DGRAM)
socketUDP.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

socketUDP.bind(("localhost", 5560))

"""def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connected = True
    while connected:
        msg_length = conn.recv(64)
    conn.close()"""

def start():
    print("STARTED")
    while True:
        weatherData , UDP_adress = socketUDP.recvfrom(2048)
        #weatherData.sendto(data, UDP_adress)
        print(weatherData)
        while True:
            encoded = weatherData.encode()
            print(encoded)
            with open("DATA.txt") as data:
                csv.writer(data).write(encoded)
            #Dersom 
            print(f'Received message from {UDP_adress}, message:')
            print(encoded)
            #print(f'Received message from {UDP_adress}, message: {data}') #Denne funker ikke, av en eller annen grunn
print("[STARTING] server is starting")
start()
