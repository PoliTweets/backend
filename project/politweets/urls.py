from django.conf import settings
from django.conf.urls import patterns
from django.conf.urls import url

from project.politweets import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^round$', views.round, name='round'),
)