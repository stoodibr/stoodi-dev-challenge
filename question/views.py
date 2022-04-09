#coding: utf8
from collections import OrderedDict
from django.shortcuts import render


def question(request):
    text = 'Quanto é 2^5?'

    # BUG: as respostas estão ficando fora de ordem
    answers = {
        'a': '0',
        'b': '2',
        'c': '16',
        'e': '128',
        'd': '32',
    }

    context = {
        'question_text': text,
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