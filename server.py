from socket import create_server

server = create_server(("localhost", 5550))
print("host")
print("Waiting for ant incomming connections...")
conn, addr = server.accept()
print(addr, "Has connected to the server")

filename = input(str("please enter the filename of the file: "))
file = open(filename , "rb")
file_data = file.read(1024)
conn.send(file_data)
print("Data has been sendt successfully!")
