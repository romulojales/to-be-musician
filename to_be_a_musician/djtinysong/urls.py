from django.conf.urls import patterns, url

from djtinysong import SONG_URL


urlpatterns = patterns('djtinysong',
    url(r'^search/(?P<params>(.+))$', 'views.search', name='tinysong_search'),
    url(r"^%s" % SONG_URL, 'views.song', name="tinysong_song")
)
