#!/usr/bin/env python

# importing libraries
from turtle import *
import turtle
# initalizing a variable for turtle
c = turtle.Turtle()
# creating turtle screen
screen = turtle.Screen()
# setting up the screen size of canvas
screen.setup(900, 650)
# changing the color of background to black
screen.bgcolor('black')
# defining speed of turtle
c.speed(5)
c.hideturtle()
# deciding the color for circle
c.fillcolor("#DC5F00")
# start the filling color
c.begin_fill()
c.up()
# radius of circle
r = 180
c.goto(0, -240)
c.circle(r)
# end filling the colour
c.end_fill()
# drawing triangle for eyes
# left eye
c.up()
c.setpos(-140, -45)
c.fillcolor("gold")
c.begin_fill()
c.forward(100)  # draw base
c.left(120)
c.forward(100)  # draw second side
c.left(120)
c.forward(100)  # draw third side
c.end_fill()
# right eye
c.up()
c.setpos(90, 40)
c.fillcolor("gold")
c.begin_fill()
c.forward(100)  # draw base
c.left(120)
c.forward(100)  # draw second side
c.left(120)
c.forward(100)  # draw third side
c.end_fill()
# drawing inverted triangle for nose
c.up()
c.setpos(0, -110)
c.fillcolor("gold")
c.begin_fill()
c.forward(40)
c.right(120)
c.forward(40)
c.right(120)
c.forward(40)
c.end_fill()
# drawing triangle for tooth of pumpkin🎃
# triangle 1
c.up()
c.setpos(-60, -120)
c.fillcolor("gold")
c.begin_fill()
c.forward(50)
c.right(120)
c.forward(50)
c.right(120)
c.forward(50)
c.end_fill()
# triangle 2
c.up()
c.setpos(-60, -120)
c.fillcolor("gold")
c.begin_fill()
c.forward(50)  # draw base
c.right(120)
c.forward(50)
c.right(120)
c.forward(50)
c.end_fill()
# trinagle 3
c.up()
c.setpos(14, -163)
c.fillcolor("gold")
c.begin_fill()
c.forward(50)  # draw base
c.right(120)
c.forward(50)
c.right(120)
c.forward(50)
c.end_fill()
# trinagle 4
c.up()
c.setpos(90, -120)
c.fillcolor("gold")
c.begin_fill()
c.forward(50)  # draw base
c.right(120)
c.forward(50)
c.right(120)
c.forward(50)
c.end_fill()
# drawing green part of pumpkin
c.fillcolor("green")
c.begin_fill()
c.goto(-20, 110)
# drawing first side
c.forward(40)  # Forward turtle by 40 units
c.left(90)  # Turn turtle by 90 degree
# drawing second side
c.forward(60)  # Forward turtle by 60 units
c.left(90)  # Turn turtle by 90 degree
# drawing third side
c.forward(40)  # Forward turtle by 40 units
c.left(90)  # Turn turtle by 90 degree
# drawing fourth side
c.forward(60)  # Forward turtle by 60 units
c.left(90)  # Turn turtle by 90 degree
c.end_fill()
# writing happy halloween on canvas
c.goto(-250, -290)
c.pencolor("red")
c.write('Happy Halloween', font=("Courier", 40, "italic"))
# holding the screen to display
screen.mainloop()
