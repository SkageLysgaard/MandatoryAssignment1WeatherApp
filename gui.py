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


def plot_list(liste):
    plt.subplot()
    plt.plot(liste)


demo_liste2 = [3,4,6,5,4,3,2,2,2,1,10,14,12,9,3,2,5]
demo_liste3 = [3,4,6,3,5,6,7,8,9,0,0,7,5,3,4,5,6,5]

plot_list(demo_liste2)
plot_list(demo_liste3)

plt.show()
