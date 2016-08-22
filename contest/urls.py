from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^contests/$', views.contests, name='contests'),
    url(r'^contest/(?P<contest_id>[0-9]+)/$', views.contest, name='contest'),  
]
