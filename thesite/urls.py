from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'thesite.views.index', name='index'),
)
