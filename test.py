from tkinter import *
win = Tk()
def cheese(x):
    print("Cheese",x)
button = Button(text = "Cheese Puffs", command = lambda: cheese("Puffs"))
button.pack()
win.mainloop()