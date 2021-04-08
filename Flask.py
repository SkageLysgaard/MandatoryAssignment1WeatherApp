from flask import Flask

#Poenget med denne filen er å ta inn værinformasjonen som blir printet,
#og på en enkel måte legge den inn som feks header på nettsiden.
#http://127.0.0.1:5000/

app = Flask(__name__)

@app.route("/<by>")
def Oslo(by):
    return f"Værmeldingen i dag i {by} er <h1>VÆRMELDINGEN<h1>"



if __name__ == "__main__":
    app.run()


print("test2")