from time import sleep
from station import StationSimulator

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
    f.write("temperature\tprecipitation")
    f.write(str(temperature) + str(precipitation))
    f.close()

    
    #print("temperature\tprecipitation")
    #for t , p in zip(temperature, precipitation):
        #print(t, "\t\t", p)
