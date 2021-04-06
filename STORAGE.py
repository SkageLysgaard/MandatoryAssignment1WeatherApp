from socket import socket, AF_INET,SOCK_STREAM, SOCK_DGRAM
from threading import Thread
import csv

socketTCP = socket(AF_INET,SOCK_STREAM)
socketUDP = socket(AF_INET,SOCK_DGRAM)

socketTCP.bind(("localhost", 5559))
socketUDP.bind(("localhost", 5560))

"""def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connected = True
    while connected:
        msg_length = conn.recv(64)
    conn.close()"""

def start():
    socketTCP.listen()
    print("[LISTENING] The server is listening...")
    while True:
        conn, TCP_addr = socketTCP.accept()
        weatherData , UDP_adress = socketUDP.recvfrom(2048)
        data = conn.recv(1024).decode()
        #ct = Thread(conn)
        encoded = data.encode()
        #Dersom inputen fra CLI er x:
        if(encoded == "1"):#Dersom meldingen fra FMI er 1 aka "rain":
                with open("DATA.txt") as data:
                    reader = csv.reader(data, delimiter = "\t")
                    for row in reader: 
                        conn.send(row[1])
        #Dersom 
        print(f'Received message from {TCP_addr, UDP_adress}, message: {data}')
        #ct.run()
        conn.close()
print("[STARTING] server is starting")
start()

