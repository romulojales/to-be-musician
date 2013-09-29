from django.test import TestCase

from __init__ import RequestJson
import djtinysong.utils
import mock


class TestSearchUtils(TestCase):

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
            musics = djtinysong.utils.search_music("arg")
            self.assertEquals(len(musics), 1)

    def test_get_with_2_objects(self):
        with  mock.patch("djtinysong.utils.get") as mck:
            mck.return_value = [{
        "Url": "http:\/\/tinysong.com\/8We2",
        "SongID": 269743,
        "SongName": "The Legend Of Lil' Beethoven",
        "ArtistID": 7620,
        "ArtistName": "Sparks",
        "AlbumID": 204019,
        "AlbumName": "Sparks"
        }, {
        "Url": "http:\/\/tinysong.com\/abc",
        "SongID": 2697431,
        "SongName": "The Legend Of Lila' Beethoven",
        "ArtistID": 76201,
        "ArtistName": "Sparkss",
        "AlbumID": 2040191,
        "AlbumName": "Sparkfs"
        }]
            musics = djtinysong.utils.search_music("abc")
            self.assertEquals(len(musics), 2)


class TestGetUtils(TestCase):

    def test_2_objects_in_response(self):
        with  mock.patch("requests.get") as mck:
            mck.return_value = RequestJson([{
        "Url": "http:\/\/tinysong.com\/8We2",
        "SongID": 269743,
        "SongName": "The Legend Of Lil' Beethoven",
        "ArtistID": 7620,
        "ArtistName": "Sparks",
        "AlbumID": 204019,
        "AlbumName": "Sparks"
        }, {
        "Url": "http:\/\/tinysong.com\/abc",
        "SongID": 2697431,
        "SongName": "The Legend Of Lila' Beethoven",
        "ArtistID": 76201,
        "ArtistName": "Sparkss",
        "AlbumID": 2040191,
        "AlbumName": "Sparkfs"
        }])
            musics = djtinysong.utils.get("abc", {})
            self.assertEquals(len(musics), 2)

    def test_throws_exception_when_request_is_bad_formated(self):
        musics = djtinysong.utils.get("aba", {})
        djtinysong.utils.API_TINYSONG_URL = ""
        musicsErro = djtinysong.utils.get("aba", {})
        self.assertNotEqual(musics, musicsErro)
