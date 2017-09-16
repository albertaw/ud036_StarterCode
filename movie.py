
class Movie():
	"""This class models a movie object"""

	def __init__(self, data):
		"""The constructor requires an object to initialize data attributes""" 
		self.title = data['title']
		self.storyline = data['storyline']
		self.poster_image_url = data['poster_image_url']
		self.trailer_youtube_url = data['trailer_youtube_url']
