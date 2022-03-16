#coding: utf8
from django.shortcuts import render

from utils.sort import sorting_answers
from utils.pagination import get_next_question

from .models import Question


def question(request, id):
    question = Question.objects.get(pk=id)
    answers_list = {
        'a': question.choice_a,
        'b': question.choice_b,
        'c': question.choice_c,
        'd': question.choice_d,
        'e': question.choice_e,
    }
   
    context = {
        'text': question.text,
        'answers_list': sorting_answers(answers_list),
        'question_id': question.id
    }

    return render(request, 'question/question.html', context=context)

def question_answer(request):
    answer = request.POST.get('answer', 'z')
    question_id = request.POST.get('question_id', '1')
    
    try:
        is_correct = answer == Question.objects.get(id=question_id).correct_answer
        context = {
        'is_correct': is_correct,
        'question_id': question_id,
        'next_question': get_next_question(question_id)
    }
    except(KeyError, Question.DoesNotExist):
        context = {
            'error_message': 'This question does not exist',
            'is_correct': False,
            'question_id': question_id
            }
        return render(request, 'question/answer.html', context=context)

    return render(request, 'question/answer.html', context=context)