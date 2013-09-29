from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from musician.views import SongStateView, MusicianView

song_state_view = login_required(SongStateView.as_view())

urlpatterns = patterns('',
    url(r'(?P<state>(learn|learning|learned))/(?P<id>\d+)/$',
        song_state_view, name='musician_song_state'),
    url(r'user/(?P<user_name>(.*))/$', MusicianView.as_view(),
        name='musician_page'),
)
