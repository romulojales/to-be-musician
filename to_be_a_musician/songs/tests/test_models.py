# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.test import TestCase
from model_mommy import mommy
from songs import models


class SongsBaseTestCase(TestCase):

    def assert_has_field(self, Model, name):
        for field in Model._meta.fields:
            if name == field.name:
                return True
        self.fail("{0} doesn't have field {1}".format(Model, name))


class SongsArtistTestCase(SongsBaseTestCase):

    @classmethod
    def setUpClass(cls):
        cls.artist = mommy.make('songs.artist', name='Metallica')

    @classmethod
    def tearDownClass(cls):
        cls.artist.delete()

    def test_string_representation(self):
        self.assertEqual(str(self.artist), 'Metallica')

    def test_slug_generation(self):
        self.assertEqual(self.artist.slug, 'metallica')

    def test_has_an_api_id_field(self):
        self.assert_has_field(models.Artist, 'api_id')


class SongsAlbumTestCase(SongsBaseTestCase):

    @classmethod
    def setUpClass(cls):
        cls.album = mommy.make('songs.album', name="Kill 'Em All")

    @classmethod
    def tearDownClass(cls):
        cls.album.delete()

    def test_string_representation(self):
        self.assertEqual(str(self.album), "Kill 'Em All")

    def test_slug_generation(self):
        self.assertEqual(self.album.slug, 'kill-em-all')

    def test_has_an_api_id_field(self):
        self.assert_has_field(models.Album, 'api_id')


class SongsSongTestCase(SongsBaseTestCase):

    @classmethod
    def setUpClass(cls):
        cls.song = mommy.make('songs.song', name='Seek and Destroy',
                              artist__name='Metallica')

    @classmethod
    def tearDownClass(cls):
        cls.song.delete()

    def test_slug_generation(self):
        self.assertEqual(self.song.slug, 'seek-and-destroy')

    def test_has_an_api_id_field(self):
        self.assert_has_field(models.Song, 'api_id')

    def test_string_representation(self):
        self.assertEqual(str(self.song), 'Seek and Destroy')

    def test_get_absolute_url(self):
        expected_url = reverse('songs_song', kwargs={
            'artist_slug': 'metallica',
            'song_slug': 'seek-and-destroy',
        })
        self.assertEqual(self.song.get_absolute_url(), expected_url)

class SongsInterpretationTestCase(SongsBaseTestCase):

    @classmethod
    def setUpClass(cls):
        cls.interpretation = mommy.make('songs.interpretation',
                                    song__name='Seek and Destroy',
                                    artist__name='Metallica',
                                    user__first_name=u'Rômulo')

    @classmethod
    def tearDownClass(cls):
        cls.interpretation.delete()
        models.Artist.objects.all().delete()
        models.Album.objects.all().delete()
        models.Song.objects.all().delete()

    def test_string_representation(self):
        self.assertEqual(unicode(self.interpretation),
                        u"Rômulo's interpretation of Seek and Destroy (Metallica)")
