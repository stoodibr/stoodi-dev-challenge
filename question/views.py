#coding: utf8
from django.shortcuts import render

from question.models import Question


def question(request):
    context = {
        'question': Question.objects.first()
    }

    return render(request, 'question/question.html', context=context)

def question_answer(request):
    answer = request.POST.get('answer', 'z')
    is_correct = answer == 'd'

    context = {
        'is_correct': is_correct,
    }

    return render(request, 'question/answer.html', context=context)