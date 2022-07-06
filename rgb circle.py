#RGB pen
import turtle as t
win = t.Screen()
pen = t.Turtle()
global color
color = 0
pen.penup()
pen.goto(0,400)
pen.pendown()
pen.speed(30)
def frame():
    global color
    if color == 16777215:
        color = 0
    else:
        color += 15
    pen.forward(5)
    pen.right(1)
    pen.color(str("0x{:06x}".format(color)).replace("0x","#"))
while True:
    frame()
