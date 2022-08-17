#coding: utf8
from django.shortcuts import get_object_or_404, render
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
        'question':questao,
        'question_num': questao.numero,
        'question_text': questao.enunciado,
        'answers': dict(sorted(answers.items())),
    }
    return render(request, 'question/question.html', context=context)


def question_answer(request):
    questao_identificador = request.POST.get('identificador', None)
    questao = get_object_or_404(Questao, identificador=questao_identificador)
    answer = request.POST.get('answer', 'Nenhuma')

    is_correct = answer == questao.alternativa_correta
    context = {
        'questao': questao,
        'answer': answer,
        'is_correct': is_correct,
    }
    return render(request, 'question/answer.html', context=context)
