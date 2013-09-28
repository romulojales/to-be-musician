from django.test import TestCase
from django.core.urlresolvers import resolve


class TestUrl(TestCase):
    urls = "djtinysong.urls"

    def test_resolution_function_for_search_view(self):
        """Test if search url is adressed to developed view"""
        url = "/search/abc"
        function = resolve(url)
        self.assertEquals(function.url_name, 'tinysong_search')
        self.assertIn("params", function.kwargs)
        self.assertEquals(function.kwargs["params"], "abc")

    def test_resolution_function_for_song_view(self):
        """Test if search url is adressed to developed view"""
        url = "/song/123"
        function = resolve(url)
        self.assertEquals(function.url_name, 'tinysong_song')
