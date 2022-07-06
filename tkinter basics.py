import tkinter as tk
window = tk.Tk()
frame = tk.Frame(background = "#000000", width = 600, height = 400)
greeting = tk.Label(frame, text = "Hello world", foreground = "#00FF00", background = "#000000")
greeting.pack()
frame.pack()
window.mainloop()
