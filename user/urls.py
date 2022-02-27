#coding: utf8
from django.urls import path
from . import views

urlpatterns = [
    path('cadastro', views.signup, name='signup'),
    path('login', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
]