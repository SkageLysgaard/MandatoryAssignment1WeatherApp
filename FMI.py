from socket import socket, create_connection, AF_INET, SOCK_STREAM

client = socket(AF_INET, SOCK_STREAM)
client.connect(("localhost", 5558))

print("[CONNECTED]")
print("Weather data:")
print(f'WRITE FOLLOWING KEYWORD TO RECEIVE CORRESPONDING DATA: \n') 
print(f'BERGEN: Receive all data from BERGEN \n')
print(f'OSLO: Receive all data from OSLO \n')
print(f'TROMSO: Receive all data from TROMSO \n \n')
print(f'DISCONNECT : Disconnects from the server')

DISCONNECT_MESSAGE = 'DISCONNECT'


while True:
    msg = str(input("Enter CITY: "))
    if (msg != DISCONNECT_MESSAGE):
        #sends the location to the server
        msg = msg.encode("utf-8")
        hello =  client.send(msg)
        msg_receievd, _ = client.recvfrom(2048)
        msg_2, _ = client.recvfrom(2048)
        msg_3, _ = client.recvfrom(2048)

        print('RECEIVING DATA: ')
        print(msg_receievd.decode())
        print(msg_2.decode())
    elif (msg == DISCONNECT_MESSAGE): 
        break






