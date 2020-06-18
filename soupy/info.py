#!/usr/bin/env python

"""This module prints the tags in data/original-bbc-in-our-times.rss to the 
screen. The tag name, attributes and string contents are printed."""

from bs4 import BeautifulSoup

def print_children(children, depth):
    ### This function is meant to be called recursively. A recursive function
    # is one that calls itself. Recursion is a common technique used for
    # dealing with nested data. The method is initially called with the first
    # level of children, within the method if a tag has children, it calls the
    # method on those children with an increase in the value of "depth"

    # Loop through each of the children passed in
    for child in children:
        # BSoup has empty tags for blank lines, we don't care about those so
        # move on to the next iteration in the loop
        if child.name is None:
            continue

        # Build a list of information that will be printed
        output = [
            depth * '    ',     # indent 4 spaces for each level of depth
            '<',
            child.name,
            ' ',
        ]

        # Optionally add information about the child's attributes and string
        # contents if it has them
        if hasattr(child, 'attrs'):
            output.append(str(child.attrs))

        if hasattr(child, 'string'):
            output.append(f' "{child.string}"')

        # join() taks the contents of a list and builds a concatenates it into
        # one big string
        print(''.join(output))

        if child.children:
            # This child tag has children, go down one more level of depth
            # (indenting the output) and handle the children
            print_children(child.children, depth + 1)


# BSoup can read from a string or a file handle to parse XML/HMTL
with open('data/original-bbc-in-our-time.rss') as handle:
    soup = BeautifulSoup(handle, 'xml')

# Call the recursive method with all of the children of the root node
print_children(soup.children, 0)
