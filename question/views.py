#coding: utf8
from django.shortcuts import render
import collections

# ordena o dict de respostas mantendo os valores originais em cada alternativa
def ordered_answers(answers):
    ordered_items = collections.OrderedDict(sorted(answers.items()))
    ordered_list = []
    for key, value in ordered_items.items():
        ordered_list.append((key, value))
    
    return dict(ordered_list)

# verifica se as respostas estão ordenadas
def check_order(answers):
    original_list_keys = list(answers)
    ordered_list_keys = sorted(answers)

    if original_list_keys != ordered_list_keys:
        return ordered_answers(answers)
    return answers


def question(request):
    text = 'Quanto é 2^5?'

    # BUG: as respostas estão ficando fora de ordem
    answers = {
        'a': '0',
        'b': '2',
        'c': '16',
        'd': '32',
        'e': '128',
    }
    checked_answers = check_order(answers)

    context = {
        'question_text': text,
        'answers': checked_answers,
    }

    return render(request, 'question/question.html', context=context)

def question_answer(request):
    answer = request.POST.get('answer', 'z')
    is_correct = answer == 'd'

    context = {
        'is_correct': is_correct,
    }

    return render(request, 'question/answer.html', context=context)