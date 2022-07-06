import turtle
import random
from math import sin, cos, radians, sqrt
screen = turtle.Screen()
screen.setup(width = 1.0, height = 1.0)
screen.bgcolor("#000000")
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(1)
pen = turtle.Turtle()
pen.width(2)
pen.speed(50)
def colour():
    return "#"+random.choice(["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"])+random.choice(["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"])+random.choice(["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"])+random.choice(["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"])+random.choice(["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"])+random.choice(["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"])
def main():
    n = random.randint(3,10)
    if n == 0:
        return False
    pen.color(colour())
    length = sqrt((400*sin(radians(180/n)))/(n*sin(radians(90-(180/n)))))*random.randint(10,30)
    slant = (length/2)/cos(radians(90-((360/n)/2)))
    pen.penup()
    pen.goto(random.randint(-960,960),random.randint(-540,540))
    pen.right(90)
    pen.right((360/n)/2)
    pen.forward(slant)
    pen.left((360/n)/2)
    pen.left(90)
    pen.pendown()
    for i in range(n):
        pen.forward(length)
        pen.left(360/n)
def end():
    screen.bye()
count = 1
while True:
    main()
    turtle.onkey(end, "Escape")
    turtle.listen()
    count += 1
    if count == 50:
        pen.clear()
        count = 0