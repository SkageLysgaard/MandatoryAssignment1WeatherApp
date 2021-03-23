from socket import socket, AF_INET, SOCK_DGRAM
import threading

sock = socket(AF_INET, SOCK_DGRAM)

host = "localhost"
port = 5050
socket_address = (host, port)
sock.bind(socket_address) 
