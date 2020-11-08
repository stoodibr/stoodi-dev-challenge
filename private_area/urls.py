from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^cadastro/$', views.SubscriptionView.as_view(), name='subscription'),
    re_path(r'^login/$', views.LoginView.as_view(), name='login'),
    re_path(r'^log-questoes/$', views.LogQuestionView.as_view(), name='log_questions'),
]
