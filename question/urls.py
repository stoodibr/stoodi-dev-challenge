#coding: utf8

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.question, name='question'),
    url(r'^resposta/$', views.question_answer, name='question_answer'),

]