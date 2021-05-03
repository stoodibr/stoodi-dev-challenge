from django.urls import path

from .views import SignUp


urlpatterns = [
    path('cadastro/', SignUp.as_view(), name='signup'),
]