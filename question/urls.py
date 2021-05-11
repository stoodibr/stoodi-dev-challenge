from django.urls import path
from.views import QuestionView

question_view = QuestionView()

urlpatterns = [
    path('', question_view.question, name='question'),
    path('resposta/', question_view.question_answer, name='question_answer'),

]
