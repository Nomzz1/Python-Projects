import turtle
import tkinter
from random import randint
from tkinter import *
from turtle import Turtle, Screen

sc=turtle.Screen()
sc.setup(600,600)

print('''Welcome to PythonBorak MkII;
Press 'c' to clear
Press 'u' to put the pen up
Press 'd' to put the pen back down
Press 'w' to change the width
Press 'v' to change colour
Press 'r' to activate rubbber''')

window = Tk()
window.title("settings")
window.minsize(250, 250)

def shap():
    print('''Press s for square
Press t for triangle
Press h for Heaxagon
Press l for circle''')

def square():
    ln = int(input("what length"))
    for i in range(4):
        a.forward(ln)
        a.left(90)

def tri():
    ln = int(input("what length"))
    for i in range(3):
        a.forward(ln)
        a.left(120)

def cir():
    a.circle(100)

def hexa():
    ln = int(input("what length"))
    for i in range(6):
        a.forward(ln)
        a.left(60)

def penup():
    a.penup()

def pd():
    a.pendown()

def rub():
    a.width(100)
    a.color("white")
   
def w():
    w = input("what do you want your width to be")
    a.width(w)
    a.speed(10000000)
   
def CC():
    colour = input("What Colour?")
    a.width(1)
    a.color(colour)
    a.speed(10000000)

def ins():
    print('''Welcome to PythonBorak MkII;
Press 'c' to clear
Press 'u' to put the pen up
Press 'd' to put the pen back down
Press 'w' to change the width
Press 'v' to change colour
Press 'r' to activate rubbber''')





def clear():
    a.reset()
    a.speed(999999)

turtle.onkey(clear,'c')
turtle.onkey(CC,'v')
turtle.onkey(w,'w')
turtle.onkey(rub,'r')
turtle.onkey(pd,'d')
turtle.onkey(penup,'u')
turtle.onkey(square,'s')
turtle.onkey(tri,'t')
turtle.onkey(hexa,'h')
turtle.onkey(cir,'l')

turtle.listen()

ButtonE = Button(window, text='Clear', command=clear)
ButtonF = Button(window, text='Change Colour', command=CC)
ButtonA = Button(window, text='Rubber', command=rub)
ButtonB = Button(window, text='width change', command=w)
ButtonC = Button(window, text='pen up', command=penup)
ButtonD = Button(window, text='pen down', command=pd)
ButtonG = Button(window, text='Print instructions', command=ins)
ButtonH = Button(window, text='shapes', command=shap)



ButtonE.pack()
ButtonF.pack()
ButtonA.pack()
ButtonB.pack()
ButtonC.pack()
ButtonD.pack()
ButtonG.pack()
ButtonH.pack()

from turtle import Turtle, Screen

screen = Screen()
a = Turtle("turtle")
a.speed(10000000)

def draging(x, y):
    a.ondrag(None)
    a.setheading(a.towards(x, y))
    a.goto(x,y)
    a.ondrag(draging)

def main():
    turtle.listen()

    a.ondrag(draging)

    turtle.onscreenclick(draging, 1)

    screen.mainloop()

while True:
    main()