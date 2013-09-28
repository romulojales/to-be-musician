from django.test import TestCase
from django.core.urlresolvers import reverse
from model_mommy import mommy
from songs import models, views


class SongsSongViewTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.artist = mommy.make('songs.artist', name='Metallica')
        cls.album = mommy.make('songs.album', name='Master of Puppets')
        cls.song = mommy.make('songs.song', name='Master of Puppets',
                              artist=cls.artist, album=cls.album)

        cls.url = reverse('songs_song', kwargs={
            'artist_slug': 'metallica',
            'song_slug': 'master-of-puppets',
        })

    @classmethod
    def tearDownClass(cls):
        cls.artist.delete()
        cls.album.delete()
        cls.song.delete()

    def setUp(self):
        self.response = self.client.get(self.url)

    def test_song_route(self):
        self.assertEqual(self.url, '/songs/metallica/master-of-puppets/')

    def test_is_available_when_have_band_and_song(self):
        self.assertEqual(self.response.status_code, 200)


class SongSongView404TestCase(TestCase):

    def test_is_unavailable_when_band_or_song_doesnt_exist(self):
        route = reverse('songs_song', kwargs={
            'artist_slug': 'megadeth',
            'song_slug': 'tornado-of-souls',
        })
        response = self.client.get(route)

        self.assertEqual(response.status_code, 404)
