from socket import socket, AF_INET,SOCK_STREAM, SOCK_DGRAM, SOL_SOCKET, SO_REUSEADDR
from threading import Thread
import csv


socketTCP = socket(AF_INET,SOCK_STREAM)
socketTCP.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
socketUDP = socket(AF_INET,SOCK_DGRAM)
socketUDP.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

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
    print("[LISTENING] The server is listening on ...")
    while True:
        conn, TCP_addr = socketTCP.accept()
        #ct = Thread(conn)
        weatherData , UDP_adress = socketUDP.recvfrom(2048)
        #ct1 = Thread(weatherData)
        data = conn.recv(1024).decode()
        weatherData.sendto(data, UDP_adress)
        if data:
            encoded = data.encode()
            #Dersom inputen fra CLI er x:
            print(data)
            if(data == "1"):#Dersom meldingen fra FMI er 1 aka "rain":
                    with open("DATA.txt") as data:
                        reader = csv.reader(data, delimiter = "\t")
                        for row in reader: 
                            pass
            #Dersom 
            print(f'Received message from {TCP_addr}, message:')
            print(encoded)
            #print(f'Received message from {UDP_adress}, message: {data}') #Denne funker ikke, av en eller annen grunn
            #ct.run()
            conn.close()
print("[STARTING] server is starting")
start()

