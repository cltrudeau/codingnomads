Turtle Exercises
================

First House
-----------

Edit the "house.py" file and use the turtle cursor to draw a simple house,
consisting of a square with a triangle on top.


     /\
    /__\
    |  |
    |__|


Length of a side should be 100 pixels. The point of the roof should be above
the square by 50 pixels and centred between the walls


House Function
--------------

Edit "fn_house.py", filling in the empty function "make_house()". The code in
the script is setup to call this function that draws houses at a specified
place and given size.

Don't forget to start the function by putting the turtle into a known state --
it could be facing in any direction or be in any spot when the function is
called.


Draw Turtle
-----------

Edit "draw_turtle.py" to use the given points to draw a turtle. 


Connect the Dots
----------------

Edit "connect.py" to create a script that reads data from a file to draw the
points contained within. The file is a CSV file with each line containing an X
and Y value separated by a comma (,). 

The "sys.argv" list contains the strings passed in on the command line. The
second item in the list is the first thing after the script name, so
"sys.argv[1]" contains whatever was passed to the program. For example, if you
run:

    $ ./connect data/join1.csv

Then "sys.argv[1]" would contain "data/join1.csv". Use this string to open
the file. Read each line from the file, parse the X and Y co-ordinates from
the line and use the points to draw what is contained in the file.

There are four CSV files in the data folder you can use to draw pictures.
