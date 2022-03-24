# coding: utf8

from django.urls import path, re_path

from . import views

urlpatterns = [
    path("cadastro/", views.RegistrationView.as_view(), name="register"),
    path("login/", views.AuthenticationView.as_view(), name="login"),
]
