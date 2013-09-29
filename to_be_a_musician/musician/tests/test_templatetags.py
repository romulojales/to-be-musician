from django.test import TestCase
from model_mommy import mommy
from musician import models
from musician.templatetags.musician_extras import learn_button


class LearnButtonTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.song = mommy.make('songs.song', name='Angel of Death')
        cls.user = mommy.make('auth.user', username='test')

    @classmethod
    def tearDownClass(cls):
        cls.song.delete()
        cls.user.delete()

    def test_state_is_empty(self):
        context = learn_button(self.user, self.song)
        self.assertEqual(context['state'], None)

    def test_learn_state(self):
        musician_song = models.Song.objects.create(user=self.user,
                                                   song=self.song,
                                                   state='learn')
        context = learn_button(self.user, self.song)
        self.assertEqual(context['state'], 'learn')

    def test_learning_state(self):
        musician_song = models.Song.objects.create(user=self.user,
                                                   song=self.song,
                                                   state='learning')
        context = learn_button(self.user, self.song)
        self.assertEqual(context['state'], 'learning')

    def test_learned_state(self):
        musician_song = models.Song.objects.create(user=self.user,
                                                   song=self.song,
                                                   state='learned')
        context = learn_button(self.user, self.song)
        self.assertEqual(context['state'], 'learned')

    def test_return_song_but_state_when_user_is_none(self):
        context = learn_button(None, self.song)
        self.assertEqual(context['song'], self.song)
        self.assertEqual(context['state'], None)
