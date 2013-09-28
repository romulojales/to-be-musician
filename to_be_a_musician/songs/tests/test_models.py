# -*- coding: utf-8 -*-
from django.test import TestCase
from model_mommy import mommy


class SongsArtistTestCase(TestCase):

    def test_string_representation(self):
        artist = mommy.make('songs.artist', name='Metallica')
        self.assertEqual(str(artist), 'Metallica')


class SongsAlbumTestCase(TestCase):

    def test_string_representation(self):
        album = mommy.make('songs.album', name="Kill 'Em All")
        self.assertEqual(str(album), "Kill 'Em All")


class SongsSongTestCase(TestCase):

    def test_string_representation(self):
        song = mommy.make('songs.song', name='Seek and Destroy')
        self.assertEqual(str(song), 'Seek and Destroy')


class SongsInterpretationTestCase(TestCase):

    def test_string_representation(self):
        interpretation = mommy.make('songs.interpretation',
                                    song__name='Seek and Destroy',
                                    artist__name='Metallica',
                                    user__first_name=u'Rômulo')

        self.assertEqual(unicode(interpretation),
                        u"Rômulo's interpretation of Seek and Destroy (Metallica)")
