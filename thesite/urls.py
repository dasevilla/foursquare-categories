from django.conf.urls import url

from thesite.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
]
