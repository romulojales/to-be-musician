from django.views.generic.base import TemplateView
from songs.models import search_songs


class SearchView(TemplateView):
    template_name = 'common/search.html'

    def get_context_data(self, **kwargs):
        q = self.request.GET.get('q')
        songs = []

        if q:
            songs = search_songs(q)

        return {'q': q, 'songs': songs}
