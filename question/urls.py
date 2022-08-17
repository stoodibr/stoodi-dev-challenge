#coding: utf8

from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.question, name='question'),
    path('<uuid:questao_identficador>', views.question, name='question_idenficated'),
    re_path(r'^resposta/$', views.question_answer, name='question_answer'),
]