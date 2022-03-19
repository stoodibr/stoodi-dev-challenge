#coding: utf8
from django.shortcuts import render

from .utils.core import sort_dict_by_keys


def question(request):
    text = 'Quanto é 2^5?'

    answers = {
        'd': '32',
        'c': '16',
        'e': '128',
        'a': '0',
        'b': '2',
    }

    answers_sorted = sort_dict_by_keys(answers)

    context = {
        'question_text': text,
        'answers': answers_sorted,
    }

    return render(request, 'question/question.html', context=context)


def question_answer(request):
    answer = request.POST.get('answer', 'z')
    is_correct = answer == 'd'

    context = {
        'is_correct': is_correct,
    }

    return render(request, 'question/answer.html', context=context)
