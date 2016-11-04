from django.conf.urls import url, include
from member import views


urlpatterns = [
    url('^$', views.index, name='index'),
]