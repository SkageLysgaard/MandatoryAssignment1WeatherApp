
import threading
import socket


host = "localhost" # localhost
port = 5550


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
