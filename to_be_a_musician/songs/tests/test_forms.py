from django.test import TestCase
from model_mommy import mommy
from songs.forms import InterpretationForm
from songs.models import Interpretation


class InterpretationFormTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user = mommy.make('auth.user', username='test')
        cls.song = mommy.make('songs.song', name='Man in the Box',
                              artist__name='Alice in Chains')

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()
        cls.song.artist.delete()
        cls.song.album.delete()
        cls.song.delete()

    def test_hide_user_field(self):
        self.assertIn('user', InterpretationForm._meta.exclude)

    def test_hide_song_field(self):
        self.assertIn('song', InterpretationForm._meta.exclude)

    def test_hide_publication_dates(self):
        self.assertIn('created_at', InterpretationForm._meta.exclude)
        self.assertIn('last_update', InterpretationForm._meta.exclude)

    def test_save_form_passing_user_and_song(self):
        form = InterpretationForm({
            'youtube_url': 'http://www.youtube.com/watch?v=ppxs4C3pu0s'
        })
        form.is_valid()
        form.save(user=self.user, song=self.song)

        interpretations = Interpretation.objects.filter(user=self.user,
                                                        song=self.song)

        self.assertEqual(len(interpretations), 1)

    def test_must_have_at_least_one_field_filled(self):
        form = InterpretationForm({})
        self.assertFalse(form.is_valid())
