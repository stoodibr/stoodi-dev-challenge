# coding: utf8

from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.QuestionView.as_view(), name="question"),
    path("<int:question_id>/", views.QuestionView.as_view(), name="question"),
]
