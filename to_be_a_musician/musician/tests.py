from django.test import TestCase
from model_mommy import mommy


class MusicianSongTestCase(TestCase):

    def test_representation_string(self):
        song = mommy.make('songs.song', name='Cowboys from Hell')
        user = mommy.make('auth.user', username='dimebag-fan')
        learning_song = mommy.make('musician.song', user=user, song=song,
                                   state='learning')

        self.assertEqual(str(learning_song),
                         'dimebag-fan is learning Cowboys from Hell')
