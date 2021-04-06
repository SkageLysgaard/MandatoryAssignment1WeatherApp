from socket import socket, create_connection

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5550))

print("connected...")
location = input("Enter your location: ")
#sends the location to the server
client.send(bytes(location, "utf-8"))

filename = "recieved_data"
file = open(filename, "wb")
file_data = client.recv(1024)
file.write(file_data)
file.close()
print("File has been recieved succsessfully!")


