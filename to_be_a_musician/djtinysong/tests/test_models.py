import unittest
from djtinysong.models import Song, search_songs
import mock


class TestModels(unittest.TestCase):

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

    def test_get_absolute_url(self):
        music = Song(SongID=123)
        self.assertEquals("/song/song/123", music.get_absolute_url())

    def test_search_musics(self):
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
            musics = search_songs("abc")
            self.assertEquals(len(musics), 1)
            self.assertEquals(musics[0].get_absolute_url(),
                              "/song/song/269743")
        