#coding: utf8
from asyncio.windows_events import NULL
from django.shortcuts import render

from question.models import Answer, LogAnswers, Question


def question(request):
    question_id= NULL
    if(request.method == 'POST'):
        question_id = request.POST.get('question_id')

    question_entity = Question.get_question(question_id)
    if(question_entity):
        answers_list = Answer.list_by_question(question_entity)

        context = {
            'question_id': question_entity.__dict__['id'],
            'question_text': question_entity.__dict__['description'],
            'answers': answers_list
        }
        return render(request, 'question/question.html', context=context)
    return render(request, 'question/no_question_available.html')

def question_answer(request):
    answer = request.POST.get('answer', 'z')
    question_id = request.POST.get('question_id')
    
    question_entity = Question.objects.get(id=question_id)
    is_correct = answer == question_entity.__dict__['correct_alternative']
    next_question_id = Question.get_next_question_id(question_id)
    
    LogAnswers.objects.create(answer=answer,is_correct=is_correct,question=question_entity)

    context = {
        'is_correct': is_correct,
        'question_id': question_id,
        'next_question_id': next_question_id
    }

    return render(request, 'question/answer.html', context=context)