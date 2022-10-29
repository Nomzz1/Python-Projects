import turtle as t
from colorsys import hls_to_rgb
win = t.Screen()
win.setup(width = 1.0, height = 1.0)
pen = t.Turtle()
pen.penup()
pen.goto(0,300)
pen.color(hls_to_rgb(0,0.5,1.0))
pen.pendown()
pen.speed("fastest")
pen.width(1)
def cw(n):
    for i in range(1,n+1):
        pen.begin_fill()
        pen.right(90)
        pen.forward(300)
        pen.left(180-(360/n))
        pen.forward(300)
        pen.right(90)
        pen.end_fill()
        pen.color(hls_to_rgb(i/n,0.5,1.0))
    pen.penup()
def end():
    win.bye()
win.onkey(end, "Escape")
win.listen()
cw(7200)
t.mainloop()
