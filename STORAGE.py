from socket import socket, AF_INET,SOCK_STREAM, SOCK_DGRAM

socketTCP = socket(AF_INET,SOCK_STREAM)
socketUDP = socket(AF_INET,SOCK_DGRAM)

socketTCP.bind(("localhost", 5555))
socketUDP.bind(("localhost", 5556))
socketTCP.listen(5)
socketUDP.listen(5)

print("[LISTENING] The server is listening...")

def start():
    while True:
        conn, addr= socketTCP.accept()
        data = conn.recv(1024).decode()
        ct = client_thread(conn)
        conn.send(new_sentence.encode())
        print(f'Received message from {addr}, message: {data}')
        ct.run()
        conn.close()

start()

