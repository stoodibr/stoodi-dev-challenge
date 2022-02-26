#coding: utf8
from django.shortcuts import render
from .classes.questions_class import *

def question(request, id = None):

    try:
        context = QuestionsRequest(id).get_context()
    except Exception as e:
        context = {
            'error_msg' : str(e)
        }

    return render(request, 'question/question.html', context=context)

def question_answer(request):
    
    questions = QuestionsRequest()
    try:
        answer, is_correct = request.POST.get('answer', None), False
        if answer:
            is_correct = questions.get_question_result(answer)

        context = {
            'is_correct': is_correct,
        }
    
    except Exception as e:
        context = {
            'error_msg' : str(e)
        }

    context['next_question'] = questions.get_next_question_id()
    context['current_question'] = questions.get_current_question()

    return render(request, 'question/answer.html', context=context)