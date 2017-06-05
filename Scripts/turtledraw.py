import turtle
import time
def draw_square():
    pen = turtle.Turtle()
    canvas = turtle.Screen()
    canvas.bgcolor("white")
    pen.shape("turtle")
    pen.color("blue")
    pen.speed(2)
    pen.forward(100)
    pen.right(90)
    pen.forward(100)
    pen.right(90)
    pen.forward(100)
    pen.right(90)
    pen.forward(100)
    pen.right(90)
    time.sleep(1)
    turtle.clear()
def draw_circle():
    pen = turtle.Turtle()
    pen.shape("arrow")
    pen.color("yellow")
    pen.speed(2)
    pen.circle(100)
    time.sleep(1)
def draw_equilateral_triangle():    
    pen = turtle.Turtle()
    pen.shape("turtle")
    pen.color("red")
    pen.speed(2)
    pen.forward(100)
    pen.left(120)
    pen.forward(100)
    pen.left(120)
    pen.forward(100)
    pen.left(120)
    time.sleep(1)

def square(me):
    for i in range (0,4):
        me.forward(100)
        me.right(90)   
        
def circle_square():
    me = turtle.Turtle()
    me.shape("turtle")
    me.color("red")
    me.speed(7)
    for i in range (0,36):
        square(me)
        me.right(10)
    me.exitonclick()     
draw_square()   
draw_circle()
draw_equilateral_triangle()
circle_square()