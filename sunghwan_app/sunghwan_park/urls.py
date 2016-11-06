from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^movie/movie_list/$', views.movie_list, name='movie_list'),
    url(r'^movie/movie_update/$', views.movie_update, name='movie_update'),
    url(r'^movie/movie_detail/(?P<movie_id>\d+)/$', views.movie_detail, name='movie_detail'),
]