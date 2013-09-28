from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView
from songs.views import SongView

urlpatterns = patterns('',
    url('(?P<artist_slug>[\w_-]+)/(?P<song_slug>[\w_-]+)/$', SongView.as_view(), name='songs_song'),
)
