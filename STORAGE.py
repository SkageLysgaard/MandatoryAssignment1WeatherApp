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
        conn, addr= socketTCP.accept()
        _ , UDP_adress = socketUDP.recvfrom(2048)
        data = conn.recv(1024).decode()
        ct = Thread(conn)
        conn.send(data.encode())
        print(f'Received message from {addr, UDP_adress}, message: {data}')
        ct.run()
        conn.close()

start()

