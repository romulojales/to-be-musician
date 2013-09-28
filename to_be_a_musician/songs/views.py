from django.views.generic.base import TemplateView
from songs.models import Song


class SongView(TemplateView):
    template_name = 'common/index.html'
