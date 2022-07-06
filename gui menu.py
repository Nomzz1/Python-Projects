from tkinter import *
import time
win = Tk()
def good():
    labelg = Label(text = "Good.")
    labelg.pack(pady = 5)
    win.after(2000, labelg.destroy)
def bad():
    labelb = Label(text = "Bad.")
    labelb.pack(pady = 5)
    win.after(2000, labelb.destroy)
def end():
    win.destroy()
label = Label(text = "You have three options:")
a = Button(text = "1: Do something good.", command = good)
b = Button(text = "2: Do something bad.", command = bad)
c = Button(text = "3: Quit.", command = end)
label.pack(pady = 5)
a.pack(pady = 5)
b.pack(pady = 5)
c.pack(pady = 5)
win.minsize(200,200)
win.mainloop()
