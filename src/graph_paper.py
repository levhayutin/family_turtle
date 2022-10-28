#!/usr/bin/env python

import turtle
import subprocess
import click

from math import remainder

def pos_top_left(turtle):
    t = turtle
    # turtle diagram
    # -1000, 500 is top left
    # 1000, 500 is top right
    # set position at top left corner
    t.penup()
    t.setx(-1000)
    t.sety(500)

def pos_center(turtle):
    t = turtle
    t.penup()
    t.setx(0)
    t.sety(0)

def draw_horizontal(turtle, direction, iterations, graph_width):
    t = turtle
    if direction == "up":
        direction = 1
    if direction == "down":
        direction = -1
    for num in range(1, iterations):
        if num == 1:
            t.setx(1000)
        t.sety(direction * num * graph_width)
        xpos = t.position()[0]
        t.pd()
        if xpos < 0:
            t.setx(1000)
        else:
            t.setx(-1000)

def draw_vertical(turtle, direction, iterations, graph_width):
    t = turtle
    if direction == "right":
        direction = 1
    if direction == "left":
        direction = -1
    print("number of iterations: " + str(iterations))
    for num in range(1, iterations):
        if num == 1:
            t.sety(500)
        t.setx(direction * num * graph_width)
        xpos = t.position()[0]
        print(xpos)
        t.pd()
        t.sety(500)
        t.sety(-500)

def draw_x(turtle, iterations, graph_width, graph_color):
    t = turtle
    # draw graph x
    pos_center(t)
    
    # draw initial line
    t.pd()
    t.pencolor("black")
    t.pensize(5)
    t.setx(1000)
    t.setx(-1000)
    t.pu()
    t.pencolor(graph_color)
    t.pensize(2)
    draw_horizontal(t, "down", iterations, graph_width)
    pos_center(t)
    draw_horizontal(t, "up", iterations, graph_width)
    t.pu()

def draw_y(turtle, iterations, graph_width, graph_color):
    t = turtle
    pos_center(t)
    t.pencolor("black")
    t.pensize(5)
    t.pd()
    t.sety(500)
    t.sety(-500)
    t.pu()
    t.pencolor(graph_color)
    t.pensize(2)
    iterations = (2 * iterations)
    draw_vertical(t, "right", iterations, graph_width)
    pos_center(t)
    draw_vertical(t, "left", iterations, graph_width)
    t.pu()

# graph_color = "#D3D3D3" # grey
# # 500 pixes / 50 = 10
# iterations = 10 # for 1/2 page
# graph_width = 50

@click.command()
@click.option('-i', '--iterations', default=10)
@click.option('-w', '--width', default=50)
@click.option('-c', '--color', default="#D3D3D3")
@click.option('-p', '--print', default=False)
def main(iterations, width, color, print):

    if remainder((1000/2),width) != 0:
        print("Sorry the width will not work w/ 1000 pixels")
    if width == 25:
        iterations=20
    elif width == 10:
        iterations=40
   
    sc = turtle.Screen()
    sc.bgcolor="white"
    sc.setup(width=1000,height=1000)
    t = turtle.Turtle()

    # set the speed
    t.speed(0)

    draw_x(t, iterations, width, color)
    draw_y(t, iterations, width, color)

    # sign :)
    t.setpos(300,-470)
    t.color("red")
    t.write("Bosas Solutions")
    turtle.update()

    if print:
        cv = turtle.getcanvas()
        cv.postscript(file="/tmp/graph.ps", colormode='color')
        subprocess.call(['lpr', '-o', 'orientation-requested=landscape', '/tmp/graph.ps'])
    turtle.done()
    turtle.exitonclick()


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter

