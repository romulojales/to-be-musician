from django.core.urlresolvers import reverse, NoReverseMatch
from django.test import TestCase
from model_mommy import mommy


class MusicianChangeStateViewTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.song = mommy.make('songs.song', name='Got the Time')

    @classmethod
    def tearDownClass(cls):
        cls.song.delete()

    def test_learn_route(self):
        url = self.get_route('learn')
        self.assertEqual(url, '/musician/learn/1/')

    def test_learning_route(self):
        url = self.get_route('learning')
        self.assertEqual(url, '/musician/learning/1/')

    def test_learned_route(self):
        url = self.get_route('learned')
        self.assertEqual(url, '/musician/learned/1/')

    def test_foreign_route(self):
        self.assertRaises(NoReverseMatch, self.get_route, 'lrenred')

    def get_route(self, state):
        return reverse('musician_song_state', kwargs={
            'id': self.song.pk,
            'state': state,
        })
