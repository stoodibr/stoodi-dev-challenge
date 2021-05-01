#coding: utf8

from django.urls import path, re_path

from question.views import Question

q = Question()

urlpatterns = [
    re_path(r'^$', q.question, name='question'),
    re_path(r'^resposta/$', q.question_answer, name='question_answer'),

]