from django.urls import path

from .views import SignUp, UserQuestions

u = UserQuestions()


urlpatterns = [
    path('cadastro/', SignUp.as_view(), name='signup'),
    path('log-questoes/', u.answered_questions, name='question_log'),
]