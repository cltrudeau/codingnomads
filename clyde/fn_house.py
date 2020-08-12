#!/usr/bin/env python

# Use what you learned in house.py to create a general house drawing function.
# Fill in make_house() so that the code underneath the __main__ block will
# work

import turtle

def make_house(clyde, start_pt, wall_length):
    """
    Fill in this function. Paramters are:
    
    :param clyde: the turtle to draw with

    :param start_pt: a tuple containing (x, y) starting point of the house,
                     the bottom left corner of the square

    :param wall_length: the length of a wall. The point of the roof should be
                        midway between the walls and half the height of a wall
                        above the top of the square
    """
    pass

if __name__ == '__main__':
    # Create a turtle named clyde
    clyde = turtle.Turtle()

    # Draw two houses
    make_house(clyde, (50, 50), 200)
    make_house(clyde, (-50, -50), 100)

    # Wait until click to leave
    turtle.exitonclick()
