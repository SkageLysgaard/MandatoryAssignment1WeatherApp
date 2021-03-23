
import threading
import socket
#is this tcp? yes/n
server = create_server(("localhost", 5550))

host = "localhost" # localhost
port = 5550

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.listen()