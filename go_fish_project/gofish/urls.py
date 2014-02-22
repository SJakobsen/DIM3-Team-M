from django.conf.urls import patterns, url
from gofish import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^login/', views.login, name='login'),
        url(r'^register/', views.register, name='register'),
        url(r'^game/', views.game, name='game'))