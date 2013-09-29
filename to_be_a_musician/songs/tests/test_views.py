from django.test import TestCase
from django.core.urlresolvers import reverse
from model_mommy import mommy
from songs import models, views


class SongsBaseViewTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.artist = mommy.make('songs.artist', name='Metallica')
        cls.album = mommy.make('songs.album', name='Master of Puppets')
        cls.song = mommy.make('songs.song', name='Master of Puppets',
                              artist=cls.artist, album=cls.album)

    @classmethod
    def tearDownClass(cls):
        cls.artist.delete()
        cls.album.delete()
        cls.song.delete()


class SongsSongViewTestCase(SongsBaseViewTestCase):

    @classmethod
    def setUpClass(cls):
        super(SongsSongViewTestCase, cls).setUpClass()

        cls.url = reverse('songs_song', kwargs={
            'artist_slug': 'metallica',
            'album_slug': 'master-of-puppets',
            'song_slug': 'master-of-puppets',
        })


    def setUp(self):
        self.response = self.client.get(self.url)

    def test_song_route(self):
        self.assertEqual(self.url, '/songs/metallica/master-of-puppets/master-of-puppets/')

    def test_is_available_when_have_band_and_song(self):
        self.assertEqual(self.response.status_code, 200)

    def test_master_of_puppets_is_in_context(self):
        self.assertEqual(self.song, self.response.context['object'])


class SongSongView404TestCase(TestCase):

    def test_is_unavailable_when_band_or_song_doesnt_exist(self):
        route = reverse('songs_song', kwargs={
            'artist_slug': 'megadeth',
            'album_slug': 'rust-in-peace',
            'song_slug': 'tornado-of-souls',
        })
        response = self.client.get(route)

        self.assertEqual(response.status_code, 404)


class SongInterpretationAddViewTestCase(SongsBaseViewTestCase):

    @classmethod
    def setUpClass(cls):
        super(SongInterpretationAddViewTestCase, cls).setUpClass()

        cls.user = mommy.make('auth.user', username='test')
        cls.user.set_password('test')
        cls.user.save()

        cls.url = reverse('songs_interpretation_add', kwargs={
            'artist_slug': 'metallica',
            'album_slug': 'master-of-puppets',
            'song_slug': 'master-of-puppets',
        })

    @classmethod
    def tearDownClass(cls):
        super(SongInterpretationAddViewTestCase, cls).tearDownClass()

        cls.user.delete()

    def setUp(self):
        self.client.login(username='test', password='test')

    def test_interpretation_add_route(self):
        self.assertEqual(self.url, '/songs/metallica/master-of-puppets/master-of-puppets/interpretation/add/')

    def test_song_is_in_context(self):
        response = self.client.get(self.url)
        self.assertIn('song', response.context)

    def test_see_the_form_when_access_by_get(self):
        response = self.client.get(self.url)
        self.assertIn('form', response.context)

    def test_saving_form(self):
        response = self.client.post(self.url, {
            'description': 'testing...',
        })
        interpretations = models.Interpretation.objects.filter(user=self.user)
        self.assertEqual(len(interpretations), 1)

    def test_redirect_after_save(self):
        response = self.client.post(self.url, {
            'description': 'testing again...',
        })
        self.assertRedirects(response, self.song.get_absolute_url())


class SongInterpretationDetailViewTestCase(SongsBaseViewTestCase):

    @classmethod
    def setUpClass(cls):
        super(SongInterpretationDetailViewTestCase, cls).setUpClass()

        cls.interpretation = mommy.make('songs.interpretation',
                                        uuid='1-2-3-4',
                                        song=cls.song)

        cls.url = reverse('songs_interpretation_detail', kwargs={
            'artist_slug': 'metallica',
            'album_slug': 'master-of-puppets',
            'song_slug': 'master-of-puppets',
            'uuid': cls.interpretation.uuid,
        })

    @classmethod
    def tearDownClass(cls):
        super(SongInterpretationDetailViewTestCase, cls).tearDownClass()

        cls.interpretation.user.delete()
        cls.interpretation.delete()

    def test_interpretation_detail_route(self):
        expected_route = "/songs/metallica/master-of-puppets/master-of-puppets/interpretation/{0}/".format(self.interpretation.uuid)
        self.assertEqual(self.url, expected_route)

    def test_object_is_in_context(self):
        response = self.client.get(self.url)
        self.assertIn('object', response.context)
        self.assertEqual(response.context['object'], self.interpretation)


class SongInterpretationUpdateViewTestCase(SongsBaseViewTestCase):

    @classmethod
    def setUpClass(cls):
        super(SongInterpretationUpdateViewTestCase, cls).setUpClass()

        cls.user = mommy.make('auth.user', username='test')
        cls.user.set_password('test')
        cls.user.save()

        cls.interpretation = mommy.make('songs.interpretation',
                                        uuid='1-2-3-4',
                                        song=cls.song, user=cls.user)

        cls.url = reverse('songs_interpretation_edit', kwargs={
            'artist_slug': 'metallica',
            'album_slug': 'master-of-puppets',
            'song_slug': 'master-of-puppets',
            'uuid': cls.interpretation.uuid,
        })

    @classmethod
    def tearDownClass(cls):
        super(SongInterpretationUpdateViewTestCase, cls).tearDownClass()

        cls.interpretation.user.delete()
        cls.interpretation.delete()

    def setUp(self):
        self.client.login(username='test', password='test')

    def test_interpretation_edit_route(self):
        expected_route = "/songs/metallica/master-of-puppets/master-of-puppets/interpretation/{0}/edit/".format(self.interpretation.uuid)
        self.assertEqual(self.url, expected_route)

    def test_song_is_in_context(self):
        response = self.client.get(self.url)
        self.assertIn('song', response.context)

    def test_see_the_form_when_access_by_get(self):
        response = self.client.get(self.url)
        self.assertIn('form', response.context)

    def test_saving_form(self):
        response = self.client.post(self.url, {
            'description': 'updating...',
        })
        updated_interpretation = (models.Interpretation
                                  .objects.get(pk=self.interpretation.pk))
        self.assertEqual(updated_interpretation.description, 'updating...')

    def test_redirect_after_save(self):
        response = self.client.post(self.url, {
            'description': 'testing again...',
        })
        self.assertRedirects(response, self.interpretation.get_absolute_url())


class SongInterpretationDeleteViewTestCase(SongsBaseViewTestCase):

    @classmethod
    def setUpClass(cls):
        super(SongInterpretationDeleteViewTestCase, cls).setUpClass()

        cls.user = mommy.make('auth.user', username='test')
        cls.user.set_password('test')
        cls.user.save()

    @classmethod
    def tearDownClass(cls):
        super(SongInterpretationDeleteViewTestCase, cls).tearDownClass()
        cls.user.delete()

    def setUp(self):
        self.interpretation = mommy.make('songs.interpretation',
                                          uuid='1-2-3-4',
                                          song=self.song, user=self.user)

        self.url = reverse('songs_interpretation_delete', kwargs={
            'artist_slug': 'metallica',
            'album_slug': 'master-of-puppets',
            'song_slug': 'master-of-puppets',
            'uuid': self.interpretation.uuid,
        })
        self.client.login(username='test', password='test')

    def tearDown(self):
        self.interpretation.delete()

    def test_interpretation_delete_route(self):
        expected_route = "/songs/metallica/master-of-puppets/master-of-puppets/interpretation/{0}/delete/".format(self.interpretation.uuid)
        self.assertEqual(self.url, expected_route)

    def test_song_is_in_context(self):
        response = self.client.get(self.url)
        self.assertIn('song', response.context)

    def test_delete_after_confirm_the_operation(self):
        response = self.client.post(self.url)
        interpretations = models.Interpretation.objects.all()
        self.assertFalse(len(interpretations))

    def test_redirect_to_song_page_after_deleting(self):
        response = self.client.post(self.url)
        self.assertRedirects(response, '/songs/metallica/master-of-puppets/master-of-puppets/')
