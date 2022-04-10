#coding: utf8
from django.shortcuts import render

from question.models import Answer, Question


def question(request):
    question_entity = Question.objects.first()
    answers_list = Answer.list_by_question(question_entity)

    question_entity_dict = question_entity.__dict__
    
    context = {
        'question_id': question_entity_dict['id'],
        'question_text': question_entity_dict['description'],
        'answers': answers_list
    }

    return render(request, 'question/question.html', context=context)

def question_answer(request):
    answer = request.POST.get('answer', 'z')
    question_id = request.POST.get('question_id')
    
    question_entity = Question.objects.values('correct_alternative').get(id=question_id)

    is_correct = answer == question_entity['correct_alternative']

    context = {
        'is_correct': is_correct,
    }

    return render(request, 'question/answer.html', context=context)