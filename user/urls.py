#coding: utf8

from django.urls import re_path

from user import views

urlpatterns = [
    re_path(r'^cadastro/$', views.signup, name='signup'),
    re_path(
        r'^cadastro/validacao/$',
        views.signup_validation,
        name='signup_validation'
    ),
    re_path(r'^login/$', views.vwlogin, name='login'),
    re_path(
        r'^login/validacao/$',
        views.login_validation,
        name='login_validation'
    ),
    re_path(r'^logout/$', views.vwlogout, name='logout'),
]
