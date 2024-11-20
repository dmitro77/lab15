from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import tkinter
import json

def graph():
    with open("task1/input.json", "r") as f:
        dict = json.load(f)
    
    sales = np.array(list(dict.values()))
    saleNames = np.array(list(dict.keys()))
    
    plt.bar(saleNames, sales)
    plt.show()

m = tkinter.Tk()
m.title("Sales manager")
m.configure(width=450, height=300, bg="salmon4") 
button = Button(m, text="Show", command=graph)
button.place(x=225, y=150)

m.mainloop()
