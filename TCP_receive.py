from flask import Flask
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
    pass


