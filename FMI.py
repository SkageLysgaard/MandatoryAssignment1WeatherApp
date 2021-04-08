from socket import socket, create_connection, AF_INET, SOCK_STREAM
#import matplotlib.pyplot as plt

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
isConnected = True

while True:
    msg = str(input("Enter CITY: "))
    if (msg != DISCONNECT_MESSAGE):
        #sends the location to the server
        #msg = msg.encode("utf-8")
        hello =  client.send(msg)
        while msg != DISCONNECT_MESSAGE:
            try: 
                msg = client.recv(2048)
            except: 
                break
            else: 
                if msg: 
                    print(msg.decode())
                else: 
                    break

            
            


        print('RECEIVING DATA: ')
        print(msg.decode())
        #stripped = msg_2.decode().split(sep=',' and '\n')
        #print(msg_2.decode())
        #print(stripped)

        
        
        """if(msg_2.decode() != 'Location,Month,Temperature,Rain'):
            Liste = []
            for obj in 
            plt.plot()"""
    elif (msg == DISCONNECT_MESSAGE): 
        client.close()
        break






