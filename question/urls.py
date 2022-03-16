#coding: utf8

from django.urls import path, re_path

from . import views

urlpatterns = [
    path('<int:id>/', views.question, name='question'),
    re_path(r'^resposta/$', views.question_answer, name='question_answer'),

]