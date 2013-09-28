from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView
from musician.views import SongStateView


urlpatterns = patterns('',
    url(r'(?P<state>(learn|learning|learned))/(?P<id>\d+)/$', SongStateView.as_view(), name='musician_song_state'),
    url(r'(?P<user_name>(.*))/$', SongStateView.as_view(), name='musician_page'),
)
