import unittest
from movie import *

class TestSolution(unittest.TestCase):
	def setUp(self):
		data = {
			'title': 'Toy Story',
			'storyline': 'Some toys come to life.',
			'poster_image_url': 'path/to/poster_image.jpg',
			'trailer_youtube_url': 'path/to/youtube_url'
		}

		self.toy_story = Movie(data)

	def test_movie_should_get_title(self):
		self.assertEqual(self.toy_story.title, 'Toy Story')

	def test_movie_should_get_storyline(self):
		self.assertEqual(self.toy_story.storyline, 'Some toys come to life.')

	def test_movie_should_get_poster_image_url(self):
		self.assertEqual(self.toy_story.poster_image_url, 'path/to/poster_image.jpg')

	def test_movie_should_get_trailer_youtube_url(self):
		self.assertEqual(self.toy_story.trailer_youtube_url, 'path/to/youtube_url')



if __name__ == '__main__':
  unittest.main()
