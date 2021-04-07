from socket import socket, create_connection, AF_INET, SOCK_STREAM

client = socket(AF_INET, SOCK_STREAM)
client.connect(("localhost", 5559))

print("[CONNECTED]")
print("Weather data:")
print("Write 1 for rain: ")
while True:
    numbers = str(input("Enter a number"))
    #sends the location to the server
    msg = numbers.encode("utf-8")
    hello =  client.send(msg)
    msg_receievd = client.recvfrom(1024)
    print(msg_receievd.decode())

"""filename = "recieved_data"
file = open(filename, "wb")
file_data = client.recv(1024)
file.write(file_data)
file.close()
print("File has been recieved succsessfully!")"""


