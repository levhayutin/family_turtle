#!/usr/bin/env python

import turtle
import time

letter_x = 300
letter_y = 350
letter_width = 50

# setup turtle screen and turtle
c = turtle.Turtle()
s = turtle.Screen()

# setup background
s.bgcolor("yellow")

# get to the initial position
c.penup()
c.setx(-800)
c.sety(400)

# draw a L
c.pd()
c.begin_fill()
c.color("blue")
c.forward(50)
c.right(90)
c.forward(350)
c.left(90)
c.forward(200)
c.right(90)
c.forward(50)
c.right(90)
c.forward(250)
c.right(90)
c.forward(400)
c.end_fill()
c.pu()

# get to the position for E
c.setx(-500)
c.sety(400)

# draw a E
# top part of E
# letter_x = 300
# letter_y = 350
# letter_width = 50
c.pd()
c.color("red")
c.begin_fill()
c.right(90)
c.forward(letter_x)
c.right(90)
c.forward(letter_width)
c.right(90)
c.forward(letter_x)
c.right(90)
c.forward(letter_width)
c.end_fill()
# bottom part of E
c.begin_fill()
c.right(180)
c.forward(letter_y + letter_width)
c.left(90)
c.forward(letter_x)
c.left(90)
c.forward(letter_width)
c.left(90)
c.forward(letter_x)
c.end_fill()
# left part of E
c.begin_fill()
c.right(180)
c.forward(letter_width)
c.left(90)
c.forward(letter_y)
c.left(90)
c.forward(letter_width)
c.end_fill()
# middle part of E
c.begin_fill()
c.left(90)
c.forward(letter_y / 2)
c.left(90)
c.forward(letter_x)
c.right(90)
c.forward(letter_width)
c.right(90)
c.forward(letter_x)
c.right(90)
c.forward(letter_width)
c.end_fill()

# Lev you now have to complete the V :)
c.pu()
c.setpos(-100.00,400.00)
c.right(90)
c.pd()
c.color("green")
c.begin_fill()
c.right(90)
c.left(22)
c.forward(100)
c.forward(100)
c.forward(100)
c.forward(100)
c.left(67)
c.left(90)
c.right(23)
c.forward(100)
c.forward(100)
c.forward(100)
c.forward(100)
c.right(67)
c.forward(10)
c.forward(10)
c.forward(10)
c.forward(10)

c.right(67)
c.left(67)
c.forward(10)
c.right(113)
c.forward(100)
c.forward(100)
c.forward(100)
c.forward(100)
c.forward(50)
c.right(67)
c.forward(50)
c.forward(50)
c.color("yellow")
c.back(20) 
c.color("green")
c.right(67)
c.forward(50)
c.forward(50)
c.forward(50)

c.right(67)
c.left(67)
c.forward(50)
c.forward(50)
c.forward(50)

c.forward(50)
c.forward(50)
c.forward(50)
c.right(23)
c.right(90)
c.forward(10)

c.forward(10)
c.forward(10)
c.forward(10)
c.forward(10)
c.forward(10)
c.forward(10)
c.end_fill()



# # Just for fun
c.penup()
c.setx(0)
c.sety(-300)
c.pen(pencolor="blue", pensize=5)
c.pendown()
c.begin_fill()
for i in range(5):
    c.forward(150)
    c.right(144)
    c.fillcolor("cyan")
c.end_fill()

breakpoint()



# leave screen up until clicked
turtle.exitonclick()
