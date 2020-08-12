#!/usr/bin/env python

import sys
import turtle

def draw_picture(points):
    """Iterate through the points list and connect each dot"""
    # Create a turtle named clyde
    clyde = turtle.Turtle()

    # Don't forget that you want to start at the first point, not wherever the
    # turtle currently is when the function is called

    # ...

if __name__ == '__main__':
    filename = sys.argv[1]
    points = []

    # Open the file named in "filename" and read each line. Each line will
    # have a string with the X and Y co-ordinates separated by a comma. Turn
    # the string values into a tuple containing int values and add them to the
    # "points" list.

    # ...

    # Call the point drawing function
    draw_picture(points)

    # Wait until click to leave
    turtle.exitonclick()
