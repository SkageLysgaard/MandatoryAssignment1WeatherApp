
import socket
import threading


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5550))

print("connected...")
location = input("Enter your location: ")
client.send(bytes(location, "utf-8"))
#location = input("Enter location to see weather: ")



filename = "recieved_data"
file = open(filename, "wb")
file_data = client.recv(1024)
file.write(file_data)
file.close()
print("File has been recieved succsessfully!")

