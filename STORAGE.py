from socket import socket, AF_INET,SOCK_STREAM, SOCK_DGRAM
from threading import Thread

socketTCP = socket(AF_INET,SOCK_STREAM)
socketUDP = socket(AF_INET,SOCK_DGRAM)

socketTCP.bind(("localhost", 5555))
socketUDP.bind(("localhost", 5556))
socketTCP.listen()


print("[LISTENING] The server is listening...")

def start():
    while True:
        conn, TCP_addr= socketTCP.accept()
        weatherData , UDP_adress = socketUDP.recvfrom(2048)
        data = conn.recv(1024).decode()
        ct = Thread(conn)
        encoded = data.encode()
        #Dersom inputen fra CLI er x:
        if(encoded == 1):
            pass
        #Dersom 
        conn.send(data.encode())
        print(f'Received message from {TCP_addr, UDP_adress}, message: {data}')
        ct.run()
        conn.close()

start()

