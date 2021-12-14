#coding: utf8

from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.question, name='question'),
    re_path('question/', views.QuestionCreateView.as_view(), name='question_create'),
    re_path('log-questoes/', views.question_logs, name='question_logs'),
    re_path(r'^resposta/(?P<id>[^/]*)/$', views.question_answer, name='question_answer'),
    re_path(r'^(?P<id>[^/]*)/$', views.question, name='question_by_id'),
]