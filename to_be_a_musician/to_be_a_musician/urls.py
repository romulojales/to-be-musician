from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

from common.views import SearchView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='common/index.html'), name='home'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^songs/', include('songs.urls')),

    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url('', include('social.apps.django_app.urls', namespace='social')),

    url(r'^admin/', include(admin.site.urls)),
)
