from django.urls import path
from user import views

urlpatterns = [
    path('cadastro/', views.create_user, name='create_user' ),
    path('login/', views.login_page, name='login_page' ),
    path('logout/', views.logout_user, name='logout' ),
]