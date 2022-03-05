#coding: utf8

from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^questao/$', views.question, name='question'),
    re_path(r'^resposta/$', views.question_answer, name='question_answer'),
    re_path(r'^cadastro/$', views.cad, name='cadastro'),
    path('', views.log , name='login'),
    re_path(r'^auth/$', views.authLogin, name='authorize'),
    # re_path(r'^$', views.log, name='login'),
    # re_path(r'^resposta/$', views.question_answer, name='question_answer'),
]