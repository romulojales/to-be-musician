from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import RequestFactory
from mock import patch
from common import views


class IndexViewTestCase(TestCase):

    def test_reverse_name(self):
        url = reverse('home')
        self.assertEqual(url, '/')


class SearchViewTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.factory = RequestFactory()

    def test_reverse_name(self):
        url = reverse('search')
        self.assertEqual(url, '/search/')

    def test_uses_search_template(self):
        self.assertEqual(views.SearchView.template_name, 'common/search.html')

    @patch('common.views.search_songs')
    def test_q_is_in_context(self, mock_search_songs):
        mock_search_songs.return_value = []

        search_view = self.get_search_view('/search/?q=megadeth')
        context = search_view.get_context_data()

        mock_search_songs.assert_called_with(u'megadeth')
        self.assertIn('q', context.keys())
        self.assertEqual(context['q'], 'megadeth')

    @patch('common.views.search_songs')
    def test_passing_q_do_a_search(self, mock_search_songs):
        mock_search_songs.return_value = [1, 2, 3, 4, 5]
        search_view = self.get_search_view('/search/?q=metallica')
        context = search_view.get_context_data()

        mock_search_songs.assert_called_with(u'metallica')
        self.assertEqual(len(context['songs']), 5)

    @patch('common.views.search_songs')
    def test_dont_search_when_hasnt_q(self, mock_search_songs):
        mock_search_songs.return_value = [1, 2, 3, 4, 5]
        search_view = self.get_search_view()
        context = search_view.get_context_data()

        self.assertFalse(context['songs'])

    def get_search_view(self, url='/search/'):
        search_view = views.SearchView()
        search_view.request = self.factory.get(url)
        return search_view
