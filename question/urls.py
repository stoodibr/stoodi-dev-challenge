#coding: utf8

from django.urls import path, re_path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name="logout"),
    
    path('', views.question, name='question'),
    path('<uuid:questao_identficador>', 
        views.question, name='question_idenficated'),
    path('resposta/', 
        views.question_answer, name='question_answer'),
]