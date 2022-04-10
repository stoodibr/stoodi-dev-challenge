#coding: utf8
from collections import OrderedDict
from django.shortcuts import render

from question.models import Question

def question(request):
    first_question = Question.objects.first()
    first_question_dict = first_question.__dict__

    answers = {
        'a': '0',
        'b': '2',
        'c': '16',
        'e': '128',
        'd': '32',
    }
    
    context = {
        'question_text': first_question_dict['description'],
        'answers': OrderedDict(sorted(answers.items()))
    }

    return render(request, 'question/question.html', context=context)

def question_answer(request):
    answer = request.POST.get('answer', 'z')
    is_correct = answer == 'd'

    context = {
        'is_correct': is_correct,
    }

    return render(request, 'question/answer.html', context=context)