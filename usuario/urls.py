from django.conf.urls import url

from .views import UsuarioRegisterView, UsuarioRegisterSuccessView

urlpatterns = [
	url(r'register/success/',UsuarioRegisterSuccessView.as_view(),name='usuario_register_success'),
	url(r'register', UsuarioRegisterView.as_view(), name='usuario_register'),
]