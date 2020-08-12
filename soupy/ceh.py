#!/usr/bin/env python

from datetime import datetime

from bs4 import BeautifulSoup

def count_word(content):
    # return 10

    # counts the words
    words = content.split(' ')
    return len(words)

# BSoup can read from a string or a file handle to parse XML/HMTL
with open('data/movies.xml') as handle:
    soup = BeautifulSoup(handle, 'xml')

# Search through the soup for all <movie> tags
num_movies = 0
total_words = 0
for movie in soup.find_all('movie'):
    num_movies += 1
    total_words += count_word(movie.description.string)

    # Movies more recent than 200 
    #
    #if int(movie.year.string) < 2000:
    #    movie.extract()

    ## If the show is not Canadian, remove the tag from the soup
    #if 'Canada' not in movie.country.string:
    #    movie.extract()

    ## Append ", eh?" to the end of every description
    #movie.description.string = movie.description.string.strip() + ', eh?'

# Print the resulting soup
#print(soup.prettify())

print(f'There {num_movies} movies')
print('Total number of words in descriptions are', total_words)
print('Average number of words in descriptions:', total_words / num_movies)
