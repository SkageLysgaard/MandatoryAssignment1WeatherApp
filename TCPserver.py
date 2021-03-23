
import threading
<<<<<<< HEAD
from socket import create_server
#is this tcp? yes
server = create_server(("localhost", 5550))
=======
import socket
>>>>>>> addet features i TCPserver

host = "localhost" 
port = 5550

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.listen()
