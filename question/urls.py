# coding: utf8

from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r"^$", views.QuestionView.as_view(), name="question"),
]
