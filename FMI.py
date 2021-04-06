from socket import socket, create_connection, AF_INET, SOCK_STREAM

client = socket(AF_INET, SOCK_STREAM)
client.connect(("localhost", 5559))

print("[CONNECTED]")
print("Weather data:")
print("Write 1 for rain")

numbers = str(input("Enter a number"))
#sends the location to the server
client.sendall(bytes(numbers, "utf-8"))

"""filename = "recieved_data"
file = open(filename, "wb")
file_data = client.recv(1024)
file.write(file_data)
file.close()
print("File has been recieved succsessfully!")"""


