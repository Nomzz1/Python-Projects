from tkinter import *
window = Tk()
window.title("Challenge 1")
instruction = Label(text = "Enter a number")
instruction.pack()
textbox = Entry(window)
textbox.pack()
listnum = Listbox()
def button():
    num = textbox.get()
    if num.isdigit() == True:
        listnum.insert(END,num)
    textbox.delete(0,END)
button1 = Button(text = "Enter", command = button)
button1.pack()
listnum.pack()
button2 = Button(text = "Clear list", command = lambda: listnum.delete(0,END))
button2.pack()
window.mainloop()