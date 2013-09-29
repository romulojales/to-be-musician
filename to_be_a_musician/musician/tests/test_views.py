from django.core.urlresolvers import reverse, NoReverseMatch
from django.test import TestCase

from model_mommy import mommy
from musician import models
from musician.models import Song


class MusicianBaseViewTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user = mommy.make('auth.user', username='test', is_active=True)
        cls.user.set_password('test')
        cls.user.save()
        cls.song = mommy.make('songs.song', name='Got the Time',
                               artist__name='Anthrax')

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()
        cls.song.delete()

    def get_route(self, state):
        return reverse('musician_song_state', kwargs={
            'id': self.song.pk,
            'state': state,
        })


class MusicianPageTestCase(MusicianBaseViewTestCase):
    def setUp(self):
        self.client.login(username='test', password='test')
        self.s = Song(user=self.user, song=self.song, state="learn")
        self.s.save()

    def tearDown(self):
        self.s.delete()

    def test_render_musics(self):
        response = self.client.get("/musician/user/test/")
        self.assertIn(self.song.name, response.content)

class MusicianLearnRoutesTestCase(MusicianBaseViewTestCase):

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


class MusicianChangeLearningStateTestCase(MusicianBaseViewTestCase):

    def setUp(self):
        self.client.login(username='test', password='test')

    def test_will_learn_a_song_state(self):
        response = self.client.get(self.get_route('learn'))
        try:
            song = models.Song.objects.get(user=self.user, song=self.song,
                                           state='learn')
        except models.Song.DoesNotExist:
            self.fail("Can't set the state of the song to learn")

    def test_is_learning_a_song_state(self):
        response = self.client.get(self.get_route('learning'))

        try:
            song = models.Song.objects.get(user=self.user, song=self.song,
                                           state='learning')
        except models.Song.DoesNotExist:
            self.fail("Can't set the state of the song to learning")

    def test_learned_a_song_state(self):
        response = self.client.get(self.get_route('learned'))

        try:
            song = models.Song.objects.get(user=self.user, song=self.song,
                                           state='learned')
        except models.Song.DoesNotExist:
            self.fail("Can't set the state of the song to learned")

    def test_redirect_to_music_page(self):
        response = self.client.get(self.get_route('learn'))
        self.assertRedirects(response, '/songs/anthrax/got-the-time/', status_code=301)

    def test_dont_duplicate_a_musician_song(self):
        self.client.get(self.get_route('learn'))
        self.client.get(self.get_route('learn'))
        songs = models.Song.objects.all()
        self.assertEqual(len(songs), 1)

    def test_dont_duplication_a_musician_song_with_different_states(self):
        self.client.get(self.get_route('learn'))
        self.client.get(self.get_route('learning'))
        self.client.get(self.get_route('learned'))

        songs = models.Song.objects.all()

        self.assertEqual(len(songs), 1)
        self.assertEqual(songs[0].state, 'learned')
