#coding: utf8
from django.shortcuts import render
from .models import Questao

def question(request):

    questao = Questao.objects.first()

    answers = {
        'a': questao.alternativa_a,
        'b': questao.alternativa_b,
        'c': questao.alternativa_c,
        'd': questao.alternativa_d,
        'e': questao.alternativa_e,
    }

    context = {
        'question_num': questao.numero,
        'question_text': questao.enunciado,
        'answers': dict(sorted(answers.items())),
    }

    return render(request, 'question/question.html', context=context)

def question_answer(request):
    answer = request.POST.get('answer', 'z')
    is_correct = answer == 'd'

    context = {
        'is_correct': is_correct,
    }

    return render(request, 'question/answer.html', context=context)
