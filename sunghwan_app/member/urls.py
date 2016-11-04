from django.conf.urls import url, include
from member import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^login', views.login, name='login'),
    url(r'^signup', views.signup, name='signup'),
]
