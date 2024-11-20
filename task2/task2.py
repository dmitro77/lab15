import tkinter
from tkinter import *

def calc(s):
    arr = [int(n) for n in s.split(",")]
    resultString = "sum: " + str(sum(arr)) + "\naverage: " + str(sum(arr) / len(arr))
    return resultString


m = tkinter.Tk()
width = 500
height = 300
m.geometry(f"{width}x{height}")
m.maxsize(width, height)
m.configure(bg="sky blue")

frame = Frame(m, bg="gray60")
frame.pack()

entry = Entry(frame)
entry.pack()

text = Text(frame, height=2, width=25)
text.pack()

button = Button(frame, text="Calculate", command=lambda: text.insert("end",calc(entry.get())))
button.pack()

m.mainloop()
