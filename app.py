from view import *
from data import data
from movie import Movie

movies = []
for movie in data:
	movies.append(Movie(movie))

open_movies_page(movies)
	
