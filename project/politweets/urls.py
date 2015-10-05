from django.conf import settings
from django.conf.urls import patterns
from django.conf.urls import url

from project.politweets import views

urlpatterns = patterns('',
    url(r'^politweets$', views.index, name='index'),
)