from django.urls import path

from . import views

urlpatterns = [
    path('cadastro/', views.register_form_view, name="register_form_view"),
    path('login/', views.login_form_view, name="login_form_view"),
    path('register/', views.register_user, name="register_user"),
    path('auth/', views.auth_user, name="auth_user"),
    path('logout/', views.logout_user, name="logout_user"),
]
