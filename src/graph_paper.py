#!/usr/bin/env python

import click
import turtle
import subprocess
import sys

from math import remainder

def pos_top_left(turtle):
    """
    Position the turtle in the upper most left corner

    Parameters
    ----------
    turtle : type turtle
        The instance of turtle 
    """
    t = turtle
    # turtle diagram
    # -1000, 500 is top left
    # 1000, 500 is top right
    # set position at top left corner
    t.penup()
    t.setx(-1000)
    t.sety(500)

def pos_center(turtle):
    """
    Position the turtle in the center at 0, 0

    Parameters
    ----------
    turtle : type turtle
        The instance of turtle 
    """
    t = turtle
    t.penup()
    t.setx(0)
    t.sety(0)

def draw_horizontal(turtle, direction, iterations, graph_width):
    """
    Draw a horizontal line across the full page -1000 to 1000 pixels

    Parameters
    ----------
    turtle : type turtle
    direction: str
        ['up', 'down']
    iterations: int
        The number of lines to draw
    graph_width: int
        Number of pixes between each line
    """
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
    """
    Draw a vertical line across the full page

    Parameters
    ----------
    turtle : type turtle
    direction: str
        ['up', 'down']
    iterations: int
        The number of lines to draw
    graph_width: int
        Number of pixes between each line
    """
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
    """
    Draw the x line

    Parameters
    ----------
    turtle : type turtle
    iterations: int
        The number of lines to draw
    graph_width: int
        Number of pixes between each line
    graph_color: string
        ["green", "blue", or "#D3D3D3"]
    """
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
    """
    Draw the y line

    Parameters
    ----------
    turtle : type turtle
    iterations: int
        The number of lines to draw
    graph_width: int
        Number of pixes between each line
    graph_color: string
        ["green", "blue", or "#D3D3D3"]
    """
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

@click.command()
@click.option('-i', '--iterations', default=10)
@click.option('-w', '--width', default=50)
@click.option('-c', '--color', default="#D3D3D3")
@click.option('-p', '--print_graph', default=False)
@click.option('-s', '--signature', default="Bosas Solutions")
def main(iterations, width, color, print_graph, signature):

    if remainder((1000/2),width) != 0:
        print("Sorry the width will not work with 1000 pixels, exiting")
        sys.exit()

    if width == 25:
        iterations=20
    elif width == 10:
        iterations=40
    elif width < 10 or width > 50:
        print_graph = False # don't waste paper :)
   
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
    t.write(signature)
    turtle.update()

    if print_graph:
        cv = turtle.getcanvas()
        cv.postscript(file="/tmp/graph.ps", colormode='color')
        subprocess.call(['lpr', '-o', 'orientation-requested=landscape', '/tmp/graph.ps'])
    turtle.done()
    turtle.exitonclick()


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter

