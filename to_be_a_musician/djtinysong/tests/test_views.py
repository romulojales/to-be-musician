import unittest

from django.test.client import Client
from django.utils import simplejson
import mock


class TestView(unittest.TestCase):

    def test_search_songs_view(self):
        with  mock.patch("djtinysong.utils.get") as mck:
            mck.return_value = [{
        "Url": "http:\/\/tinysong.com\/8We2",
        "SongID": 269743,
        "SongName": "The Legend Of Lil' Beethoven",
        "ArtistID": 7620,
        "ArtistName": "Sparks",
        "AlbumID": 204019,
        "AlbumName": "Sparks"
        }]
            client = Client()
            response = client.get("/song/search/Legend")
            musics = simplejson.loads(response.content)
            self.assertEquals(len(musics), 1)
            self.assertEquals(musics[0]["url"],
                              "/song/song/269743")
