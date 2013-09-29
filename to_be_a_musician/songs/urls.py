from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from songs.views import (InterpretationView, InterpretationCreateView,
                         InterpretationDeleteView, InterpretationUpdateView,
                         SongView)

SONG_URL_PATTERN = '(?P<artist_slug>[\w_-]+)/(?P<song_slug>[\w_-]+)'

interpretation_create_view = login_required(InterpretationCreateView.as_view())
interpretation_update_view = login_required(InterpretationUpdateView.as_view())
interpretation_delete_view = login_required(InterpretationDeleteView.as_view())

urlpatterns = patterns('',
    url(r"{0}/interpretation/add/$".format(SONG_URL_PATTERN),
        interpretation_create_view, name='songs_interpretation_add'),
    url(r"{0}/interpretation/(?P<id>\d+)/$".format(SONG_URL_PATTERN),
        InterpretationView.as_view(), name='songs_interpretation_detail'),
    url(r"{0}/interpretation/(?P<id>\d+)/edit/$".format(SONG_URL_PATTERN),
        interpretation_update_view, name='songs_interpretation_edit'),
    url(r"{0}/interpretation/(?P<id>\d+)/delete/$".format(SONG_URL_PATTERN),
        interpretation_delete_view, name='songs_interpretation_delete'),

    url(r"{0}/$".format(SONG_URL_PATTERN), SongView.as_view(),
        name='songs_song'),
)
