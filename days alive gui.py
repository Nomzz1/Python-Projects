# Import needed modules
import datetime as dt
import tkinter as tk
# Create and configure window
win = tk.Tk()
win.maxsize(250,500)
win.minsize(250,500)
win.configure(bg = "#3c3f43")
win.title("Days Alive Calculator")
# Create question label and entry fields
question = tk.Label(text = "Please enter your date of birth in the", bg = "#3c3f43", fg = "#ffffff")
question2 = tk.Label(text = "fields below in the form dd/mm/yyyy.", bg = "#3c3f43", fg = "#ffffff")
question.pack()
question2.pack()
dayEntry = tk.Entry(width = 2)
monthEntry = tk.Entry(width = 2)
yearEntry = tk.Entry(width = 4)
dayLabel = tk.Label(text = "Day:", bg = "#3c3f43", fg = "#ffffff")
monthLabel = tk.Label(text = "Month:", bg = "#3c3f43", fg = "#ffffff")
yearLabel = tk.Label(text = "Year:", bg = "#3c3f43", fg = "#ffffff")
buffer = tk.Label(text = "....", bg = "#3c3f43", fg = "#ffffff")
dayLabel.pack()
dayEntry.pack()
monthLabel.pack()
monthEntry.pack()
yearLabel.pack()
yearEntry.pack()
buffer.pack()
# Create button with function to accept inputs and output calculated answers
def func():
    day = int(dayEntry.get())
    month = int(monthEntry.get())
    year = int(yearEntry.get())
    bday = dt.datetime(year, month, day)
    today = dt.datetime.now()
    diff = today - bday
    if diff.days != 1:
        l1 = tk.Label(win, text = f"You have been alive for {diff.days} day.", bg = "#3c3f43", fg = "#ffffff").pack()
    else:
        l1 = tk.Label(text = f"You have been alive for {diff.days} day.", bg = "#3c3f43", fg = "#ffffff").pack()
    l2 = tk.Label(text = f"You have been alive for {diff.days * 24} hours.", bg = "#3c3f43", fg = "#ffffff").pack()
    l3 = tk.Label(text = f"You have been alive for {diff.days * 24 * 60} minutes.", bg = "#3c3f43", fg = "#ffffff").pack()
    l4 = tk.Label(text = f"You have been alive for {diff.days * 24 * 60 * 60} seconds.", bg = "#3c3f43", fg = "#ffffff").pack()
button = tk.Button(text = "Enter.", command = func)
button.pack()
win.mainloop()
