from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import RequestFactory
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

    def test_q_is_in_context(self):
        search_view = self.get_search_view('/search/?q=megadeth')
        context = search_view.get_context_data()

        self.assertIn('q', context.keys())
        self.assertEqual(context['q'], 'megadeth')

    def test_passing_q_do_a_search(self):
        search_view = self.get_search_view('/search/?q=metallica')
        context = search_view.get_context_data()

        self.assertEqual(len(context['songs']), 5)
        self.assertEqual(context['songs'][0].songId, '1')

    def test_dont_search_when_hasnt_q(self):
        search_view = self.get_search_view()
        context = search_view.get_context_data()

        self.assertFalse(context['songs'])

    def get_search_view(self, url='/search/'):
        search_view = views.SearchView()
        search_view.request = self.factory.get(url)
        return search_view
