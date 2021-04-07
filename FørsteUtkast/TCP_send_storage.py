from flask import Flask
from socket import socket, AF_INET, SOCK_STREAM

app = Flask(__name__)

@app.route("/location")
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
    


