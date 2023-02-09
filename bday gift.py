from tkinter import Label, Entry, Button, Tk, W, Frame, EW
from random import randint

win = Tk()

nameContainer = Frame(win)
nameLabel = Label(nameContainer, text = "Name:")
nameEntry = Entry(nameContainer, width = 20)
nameLabel.grid(column=0,row=0,padx=2,pady=2,sticky = W)
nameEntry.grid(column=1,row=0,padx=2,pady=2,sticky = W)
nameContainer.grid(column=0,row=0,padx=2,pady=2,sticky = W)

ageContainer = Frame(win)
ageLabel = Label(ageContainer, text = "Age:")
ageEntry = Entry(ageContainer, width = 3)
ageLabel.grid(column=0,row=0,padx=2,pady=2,sticky = W)
ageEntry.grid(column=1,row=0,padx=2,pady=2,sticky = W)
ageContainer.grid(column=0,row=1,padx=2,pady=2,sticky = W)


inflationContainer = Frame(win)
inflationLabel = Label(inflationContainer, text = "Inflation:")
inflationEntry = Entry(inflationContainer, width = 6)
inflationLabel2 = Label(inflationContainer, text = "%")
inflationLabel.grid(column=0,row=0,padx=2,pady=2,sticky = W)
inflationLabel2.grid(column=2,row=0,padx=0,pady=2,sticky = W)
inflationEntry.grid(column=1,row=0,padx=2,pady=2,sticky = W)
inflationContainer.grid(column=0,row=2,padx=2,pady=2,sticky = W)

def calculate():
    perYear = 0.67
    total = (25 * (1 + float(inflationEntry.get())/100)) + (int(ageEntry.get()) * perYear)
    final = Label(text = f"Birthday gift for {nameEntry.get()} is £{total:.2f}")
    final.grid(column=0,row=4,padx=2,pady=2,sticky = EW, columnspan=3)

calcButton = Button(text = "Calculate!", command = calculate)
calcButton.grid(column=0,row=3,padx=2,pady=2)

win.mainloop()