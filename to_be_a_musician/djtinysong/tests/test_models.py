import unittest
from djtinysong.models import Song


class TestView(unittest.TestCase):

    def test_simple_class_instance(self):
        dictionary = {
        "Url": "http:\/\/tinysong.com\/8We2",
        "SongID": 269743,
        "SongName": "The Legend Of Lil' Beethoven",
        "ArtistID": 7620,
        "ArtistName": "Sparks",
        "AlbumID": 204019,
        "AlbumName": "Sparks"
        }

        music = Song(**dictionary)
        self.assertEquals(music.tinySongURL, dictionary["Url"])
        self.assertEquals(music.songId, dictionary["SongID"])
        self.assertEquals(music.songName, dictionary["SongName"])
        self.assertEquals(music.artistId, dictionary["ArtistID"])
        self.assertEquals(music.artistName, dictionary["ArtistName"])
        self.assertEquals(music.albumId, dictionary["AlbumID"])
        self.assertEquals(music.albumName, dictionary["AlbumName"])
