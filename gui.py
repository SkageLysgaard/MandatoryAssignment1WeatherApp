import tkinter as tk
from tkinter import *
import os
import random
import matplotlib.pyplot as plt

# label = tk.Label(
#     text="Vår værstasjon",
#     fg="white",
#     bg="LightSkyBlue1",
#     width=125,
#     height=50
# )


def plot_temp(liste, index):
    plt.subplot(1, 2, index)
    plt.plot(liste)
    plt.xlabel('Tid')
    plt.ylabel('Temperatur')
    plt.title(f'Temperaturer i {location} for {month}')

def plot_rain(liste, index):
    plt.subplot(1, 2, index)
    plt.plot(liste)
    plt.xlabel('Tid')
    plt.ylabel('Regn')
    plt.title(f'Regnmengde i {location} for {month}')


demo_liste2 = [3,4,6,5,4,3,2,2,2,1,10,14,12,9,3,2,5]
demo_liste3 = [3,4,6,3,5,6,7,8,9,0,0,7,5,3,4,5,6,5]

month = 'Mai'
location = 'Oslo'

plot_temp(demo_liste2,1)
plot_rain(demo_liste3,2)


plt.show()