from socket import socket, create_connection, AF_INET, SOCK_STREAM

client = socket(AF_INET, SOCK_STREAM)
client.connect(("localhost", 5558))

print("[CONNECTED]")
print("Weather data:")
print(f'WRITE FOLLOWING KEYWORD TO RECEIVE CORRESPONDING DATA: \n') 
print(f'BERGEN: Receive all data from BERGEN \n')
print(f'OSLO: Receive all data from OSLO \n')
print(f'TROMSO: Receive all data from TROMSO \n')


while True:
    numbers = str(input("Enter CITY: "))
    #sends the location to the server
    msg = numbers.encode("utf-8")
    hello =  client.send(msg)
    msg_receievd, _ = client.recvfrom(2048)
    msg_2, _ = client.recvfrom(2048)
    msg_3, _ = client.recvfrom(2048)

    print('RECEIVING DATA: ')
    print(msg_receievd.decode())
    print(msg_2.decode())






