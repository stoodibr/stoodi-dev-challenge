#coding: utf8
from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.question, name='question'),
    path('<int:id>', views.question, name='question_by_id'),
    re_path(r'^resposta/$', views.question_answer, name='question_answer'),
    path('log-questoes', views.log_by_user, name='user_log'),
]