import unittest
from unittest.mock import patch
from model import Request

from opengraph import OpenGraph


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.example_document = """
            <html prefix="og: https://ogp.me/ns#">
            <head>
            <title>The Rock (1996)</title>
            <meta property="og:title" content="The Rock" />
            <meta property="og:type" content="video.movie" />
            <meta property="og:description" content="Description movie The Rock" />
            <meta property="og:url" content="https://www.imdb.com/title/tt0117500/" />
            <meta property="og:image" content="https://ia.media-imdb.com/images/rock.jpg" />
            <meta property="og:site_name" content="IMDB" />
            ...
            </head>
            ...
            </html>
        """

    def test_get_tags(self):
        """Test on geting all tags."""
        with patch('opengraph.OpenGraph') as mock_get_req:
            instance = mock_get_req.return_value
            instance.get_req.return_value = Request(self.example_document, 200)
            thing = OpenGraph('https://test.com')

            self.assertEqual(thing.tags.title, 'The Rock')


if __name__ == '__main__':
    unittest.main()
