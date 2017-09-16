from view import *
from data import data
from movie import Movie

movies = []

# initialize list of movies
for movie in data:
	movies.append(Movie(movie))

""" load movies into web page and open browser"""
open_movies_page(movies)
	
