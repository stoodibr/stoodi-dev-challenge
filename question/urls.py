#coding: utf8

from django.urls import path

from . import views

urlpatterns = [    
    path('', views.question, name='question'),
    path('<uuid:questao_identficador>', 
        views.question, name='question_idenficated'),
    path('resposta/', 
        views.question_answer, name='question_answer'),
    path('log-questoes/', 
        views.log_usuario_questoes, name='log_questoes'),
]