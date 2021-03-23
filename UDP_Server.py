import threading
from socket import socket, AF_INET, SOCK_DGRAM

HEADER = 64
sock = socket()
SERVER = ("localhost", 5550)
ADDR = (SERVER)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket(AF_INET,SOCK_DGRAM)
server.bind(ADDR)



def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        print(msg_length)
        msg_length = msg_length
        
        msg_length = True
        if msg_length:
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")
print("[STARTING] server is starting")
start()