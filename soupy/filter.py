#!/usr/bin/env python

"""This module parses data/simple-bbc.rss, processing each of the items in the
file.  Titles with "(repeat)" in them are removed, all others have their
date tag replaced with ISO 8601 format. The result is printed to the screen."""

from datetime import datetime

from bs4 import BeautifulSoup

# BSoup can read from a string or a file handle to parse XML/HMTL
with open('data/simple-bbc.rss') as handle:
    soup = BeautifulSoup(handle, 'xml')

# Search through the soup for all <item> tags
for item in soup.find_all('item'):

    # If the show is a repeat, remove the tag from the soup
    if '(repeat)' in item.title.string:
        item.extract()

    # Parse the show's horrible date format and replace it with something sane
    #
    # E.g. <pubDate>Thu, 07 May 2020 09:15:00 +0000</pubDate> 
    #        becomes
    #      <pubDate>2020/05/07 09:15:00 +0000</pubDate> 
    when = datetime.strptime(item.pubDate.string, '%a, %d %b %Y %H:%M:%S %z')
    item.pubDate.string = when.strftime('%Y/%m/%d %H:%M:%S %z')

# Print the resulting soup
print(soup.prettify())
