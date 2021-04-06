from socket import create_server
from time import sleep
from station import StationSimulator

server = create_server(("localhost", 5550))
print("host")
print("Waiting for ant incomming connections...")
conn, addr = server.accept()
location = conn.recv(1024).decode()
print(addr, "Has connected to the server", location)
 
 


#if filename == bergen:
if __name__ == "__main__":
    bergen_station = StationSimulator(simulation_interval=1)
    bergen_station.turn_on()

    temperature = []
    precipitation = []

    for _ in range(72):
        # Sleep for 1 second to wait for new weather data
        # to be simulated
        sleep(1)
        # Read new weather data and append it to the
        # corresponding list
        temperature.append(bergen_station.temperature)
        precipitation.append(bergen_station.rain)

    bergen_station.shut_down()
    
    f = open("bergen.py", "w")
    f.write("temperature " + str(temperature) + "\n")
    f.write("precipitation " + str(precipitation))
    f.close()
else:
    print("Sorry, i didn't get that")

    

filename = location
file = open(filename , "rb")
file_data = file.read(1024)
conn.send(file_data)
print("Data has been sendt successfully!")
