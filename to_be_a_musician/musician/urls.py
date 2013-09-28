from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView


urlpatterns = patterns('',
    url(r'(?P<state>(learn|learning|learned))/(?P<id>\d+)/$', TemplateView.as_view(template_name='common/index.html'), name='musician_song_state'),
)
