from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from app import views
from .views import *



urlpatterns = [
    path("index/",index),
    path("client/name/",client_name_view),
    path("add/users/project/", adduser_view),
    path("logout/",logout_view),
    url(r'^project/(?P<pk>[0-9]+)/$', views.project_detail),
    url(r'^project/$', views.project_list),

    url(r'^client/(?P<pk>[0-9]+)/$', views.client_detail),
    url(r'^client/$', views.client_list),

]

urlpatterns = format_suffix_patterns(urlpatterns)
