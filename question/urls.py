#coding: utf8

from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>/', views.question, name='question'),
    path('resposta/', views.question_answer, name='question_answer'),
]