from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^movie/movie_list/$', views.movie_list, name='movie_list'),
]