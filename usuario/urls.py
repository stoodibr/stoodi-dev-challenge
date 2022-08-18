#coding: utf8

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import CadastroView

urlpatterns = [    
    path('login/', LoginView.as_view(template_name='usuario/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
]