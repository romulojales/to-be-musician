
import unittest
from djtinysong.utils import search_music
import mock


class TestUtils(unittest.TestCase):
    def test_simple_search(self):
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
            musics = search_music("arg")
            self.assertEquals(len(musics), 1)
