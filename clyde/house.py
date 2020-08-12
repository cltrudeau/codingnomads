#!/usr/bin/env python

import turtle

clyde = turtle.Turtle()

# Clyde the turtle starts at position 0, 0 and facing East
#
# 1) Move the turtle forward by 100 to draw the floor
# 2) Turn left 90 degrees 
# 3) Move forward by 100 to draw the left wall
# ... continue until you've drawn the square

clyde.forward(100)
clyde.left(90)
clyde.forward(100)
# ...


# The top left corner of the square is at (0, 100)
# Lift the pen and move to that point
# The roof is at (50, 150), put the pen down and draw to that point
# ... finish the roof by drawing to the top right corner

clyde.penup()
clyde.goto( (0, 100) )
clyde.pendown()
clyde.goto( (50, 150) )
# ...

# Wait until click to leave
turtle.exitonclick()
