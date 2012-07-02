from django.conf.urls import patterns, include, url

urlpatterns = patterns('slander.views',
    url(r'^$', 'index'),
    url(r'^(?P<id>[a-zA-Z][a-zA-Z0-9_]{4,})$', 'id'),
)