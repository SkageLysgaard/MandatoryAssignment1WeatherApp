import tkinter as tk
from tkinter import *
import os
import random
import matplotlib.pyplot as plt

label = tk.Label(
    text="Vår værstasjon",
    fg="white",
    bg="LightSkyBlue1",
    width=125,
    height=50
)


def get_weatherdata(city):
    pass


demo_liste = [3,4,6,5,4,3,2,2,2,1,10,14,12,9,3,2,5]
length = len(demo_liste)

plt.plot(demo_liste)

plt.show()
