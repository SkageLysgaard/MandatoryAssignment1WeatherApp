from flask import Flask
from socket import socket, AF_INET, SOCK_STREAM

<<<<<<< HEAD
sock = socket()
sock.bind(("localhost", 5555))

sock.listen()
print("[LISTENING TO COMMANDS] The storage is listening....")

=======
>>>>>>> fd02503e4c75112b448200b2e3bff5ab0f7c42e7
app = Flask(__name__)

@app.route("location")
def recieveLocation():
    pass
@app.route("month")
def recieveMonth():
    pass
@app.route("temperature")
def recieveTemperature():
    pass
@app.route("rain")
def recieveRain():
<<<<<<< HEAD
    pass
=======
    
>>>>>>> fd02503e4c75112b448200b2e3bff5ab0f7c42e7


