from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^cadastro/$', views.sign_up, name='sign_up'),
    re_path(r'^login/$', views.sign_in, name='sign_in'),

]
