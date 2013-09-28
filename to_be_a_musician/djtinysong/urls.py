from django.conf.urls import patterns, include, url


urlpatterns = patterns('djtinysong',
    url(r'^search/(?P<params>(.+))$', 'views.search', name='tinysong_search'),
    )
