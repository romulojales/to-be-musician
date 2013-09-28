from django.test import TestCase
from django.core.urlresolvers import reverse
from songs import models


class SongsSongViewTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = reverse('songs_song', kwargs={
            'artist_slug': 'metallica',
            'song_slug': 'master-of-puppets',
        })

    def test_song_route(self):
        self.assertEqual(self.url, '/songs/metallica/master-of-puppets/')
