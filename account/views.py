import ast

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from selecao import settings


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class UserQuestions:

    def answered_questions(self, request):
        questions = []
        user = request.user.username

        if user != '':
            file_log = open(f'{settings.BASE_DIR}/answered_questions.log', 'r')
            lines = file_log.read().splitlines()

            for line in lines:
                if not line:
                    continue

                col = line.split('question_answer: ')
                if len(col) == 2:
                    question_dict = ast.literal_eval(col[1])
                    if question_dict.get('user') == user:
                        questions.append(line)

            file_log.close()

        context = {
            'questions': questions, 
            'user': user,
        }

        return render(request, 'answered_question/answered_question.html', context=context)
