from django.conf.urls import patterns, url

from musician.views import SongStateView, MusicianView


urlpatterns = patterns('',
    url(r'(?P<state>(learn|learning|learned))/(?P<id>\d+)/$',
        SongStateView.as_view(), name='musician_song_state'),
    url(r'user/(?P<user_name>(.*))/$', MusicianView.as_view(),
        name='musician_page'),
)
