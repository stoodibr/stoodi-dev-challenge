#coding: utf8
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import Questao, Resposta

def question(request, questao_identficador=None):
    if questao_identficador:
        questao = get_object_or_404(Questao, identificador=questao_identficador, ativa=True)
    else:
        questao = Questao.objects.filter(
            ativa=True
            ).order_by('numero', 'pk').first()

    if not questao:
        raise Http404

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
    
    proximo = Questao.objects.filter(
        ativa=True, 
        numero__gte=questao.numero,
        ).exclude(pk=questao.pk).order_by('numero', 'pk').first()

    if not proximo:
        proximo =  Questao.objects.filter(
        ativa=True
        ).order_by('numero', 'pk').first()
    
    Resposta.objects.create(
        questao=questao,
        alternativa_escolhida=answer,
        alternativa_correta=is_correct)

    context = {
        'proxima_questao': proximo,
        'questao': questao,
        'answer': answer,
        'is_correct': is_correct,
    }
    return render(request, 'question/answer.html', context=context)
