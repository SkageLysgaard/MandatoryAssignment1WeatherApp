from socket import socket, create_connection, AF_INET, SOCK_STREAM
import json
import ast
import matplotlib.pyplot as plt
#import matplotlib.pyplot as plt

client = socket(AF_INET, SOCK_STREAM)
client.connect(("localhost", 5557))

def plot_temp(liste, index, location, month):
    plt.subplot(1, 2, index)
    plt.plot(liste)
    plt.xlabel('Tid')
    plt.ylabel('Temperatur')
    plt.title(f'Temperaturer i {location} for {month}')

def plot_rain(liste, index, location, month):
    plt.subplot(1, 2, index)
    plt.plot(liste)
    plt.xlabel('Tid')
    plt.ylabel('Regn')
    plt.title(f'Regnmengde i {location} for {month}')   


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
    if(msg == False): break
    sent = client.send(msg.encode())
    if (msg != DISCONNECT_MESSAGE):
        #sends the location to the server
        #msg = msg.encode("utf-8")
            
        while msg != DISCONNECT_MESSAGE:
            try: 
                msg = client.recv(2048) 
            except: 
                break
            else: 
                if msg: 
                    print('RECEIVING DATA: ')
                    decoded = msg.decode()
                    liste = ast.literal_eval(decoded)
                    for obj in liste:
                        obje = json.loads(obj[0])
                        temp_list = obje['TEMPERATURE']
                        rain_list = obje['RAIN']
                        location = obje['LOCATION']
                        month = obje['MONTH']
                        plot_temp(temp_list, 1, location, month)
                        plot_temp(rain_list, 2, location, month)
                        plt.show()

                        print('RECIEVED DATA: TEMP: ' + temp_list)
                        print('RECIEVED DATA: TEMP: ' + rain_list)
                else: 
                    break
                    

        

        #stripped = msg_2.decode().split(sep=',' and '\n')
        #print(msg_2.decode())
        #print(stripped)

        






