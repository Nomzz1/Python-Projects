from tkinter import Entry, DoubleVar, Label, Tk

win = Tk()

f = DoubleVar()
c = DoubleVar()

fEntry = Entry(textvariable = f)
cEntry = Entry(textvariable = c)

fLabel = Label(text = "Farenheit:")
fResult = Label()

cLabel = Label(text = "Celsius:")
cResult = Label()

in_set = False

def FtoC(*args):
    global in_set
    if not in_set:
        try:
            farenheit = float(f.get())
        except:
            farenheit = 0
        in_set = True
        c.set(float((farenheit - 32)*5/9))
        in_set = False

def CtoF(*args):
    global in_set
    if not in_set:
        try:
            celsius = float(c.get())
        except:
            celsius = 0
        in_set = True
        f.set(float((9/5*celsius)+32))
        in_set = False

f.trace_add("write", FtoC)
c.trace_add("write", CtoF)

fLabel.grid(column = 0, row = 0)
fEntry.grid(column = 1, row = 0)

cLabel.grid(column = 0, row = 1)
cEntry.grid(column = 1, row = 1)

win.mainloop()
