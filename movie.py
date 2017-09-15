
class Movie():
	def __init__(self, data):
		self.title = data['title']
		self.storyline = data['storyline']
		self.poster_image_url = data['poster_image_url']
		self.trailer_youtube_url = data['trailer_youtube_url']
