from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<id>\d+)/add$', views.add_course),
    url(r'^(?P<id>\d+)/delete$', views.delete),
    url(r'^(?P<id>\d+)/process_edit$', views.process_edit),
    url(r'^(?P<id>\d+)/edit$', views.edit),
    url(r'^(?P<id>\d+)/join$', views.join),
    url(r'^(?P<id>\d+)/show$', views.show),
    url(r'^(?P<id>\d+)/show$', views.show),
]