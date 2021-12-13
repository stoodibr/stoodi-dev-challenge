#coding: utf8

from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^cadastro/$', views.register, name='register'),
    re_path(r'^login/$', views.login_page, name='login'),
    re_path(r'^logout/$', views.logout_page, name='logout'),
]