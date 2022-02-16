#coding: utf8
from django.http import JsonResponse
from django.shortcuts import render
from question.models import Pergunta,historicoPerguntas
from usuario.models import Usuario

def question(request):
    # BUG: as respostas estão ficando fora de ordem
    pergunta_id = request.GET.get("pergunta",None)
    pergunta_db = Pergunta.objects.all()
    try:
        if pergunta_id is not None:
            _pergunta = Pergunta.objects.filter(id=int(pergunta_id)).first()
        else:
            _pergunta = pergunta_db.first()
        context = {
            "question_text":_pergunta.texto,
            "answers":{
                "a":_pergunta.opcao_A,
                "b":_pergunta.opcao_B,
                "c":_pergunta.opcao_C,
                "d":_pergunta.opcao_D,
                "e":_pergunta.opcao_E
                },
        }

        if pergunta_db.count() > 1:
            try:
                proxima_pergunta = pergunta_db.get(id=_pergunta.id + 1 )
            except:
                proxima_pergunta = Pergunta.objects.all().first()

            context["next"] = proxima_pergunta.id
    except:
        context = {}
    return render(request, 'question/question.html', context=context)
    

def question_answer(request):
    answer = request.POST.get('answer', 'z')
    pergunta = request.POST.get("pergunta",None)
    #usuario_id = request.POST.get("usuario",None)
    _pergunta = Pergunta.objects.filter(texto=pergunta).first()
    
    #try:
    #    _usuario = Usuario.objects.filter(id=int(usuario_id)).first()
    #except:
    #    _usuario = None

    if answer.upper() == _pergunta.resposta:
        is_correct = True
    else:
        is_correct = False
    
    context = {
        'is_correct': is_correct,
    }
    #log
    nova_resposta = historicoPerguntas()
    nova_resposta.pergunta = _pergunta.texto
    nova_resposta.correto = is_correct
    nova_resposta.alternativa_escolhida = answer
    #nova_resposta.user = _usuario if _usuario is not None else None 
    nova_resposta.save()

    return render(request, 'question/answer.html', context=context)


def  log_questoesview(request):
    usuario_id = request.GET.get("usuario",None)
    log_respostas = historicoPerguntas.objects.filter(user=int(usuario_id))
    context = {}
    result = []
    for resposta in log_respostas:
        result.append({
            "pergunta": resposta.pergunta,
            "correto":resposta.correto ,
            "alternativa_escolhida": resposta.alternativa_escolhida,
            "user": resposta.user.nome if resposta.user else None,
        })
    
    
    return JsonResponse(
        status=200, data={"dados": context, "count": log_respostas.count()}
    )
        