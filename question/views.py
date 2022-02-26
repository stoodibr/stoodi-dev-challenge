#coding: utf8
from django.shortcuts import render
from .classes.questions_class import *
from .classes.custom_logs import CustomLogs

def question(request, id = None):

    try:
        context = QuestionsRequest(id).get_context()
    except Exception as e:
        context = {
            'error_msg' : str(e)
        }

    return render(request, 'question/question.html', context=context)

def question_answer(request):
   
    try:
        logger = CustomLogs()
        questions = QuestionsRequest()
        answer, is_correct = request.POST.get('answer', None), False
        if answer:
            is_correct, current_answer_text = questions.get_question_result(answer)
            
            logger.add_log( answer= f"{answer} - {current_answer_text}" , is_correct=is_correct)

        context = {
            'is_correct': is_correct,
        }
    
        context['next_question'] = questions.get_next_question_id()
        context['current_question'] = questions.get_current_question()
           
    except Exception as e:
        context = {
            'error_msg' : str(e)
        }

    return render(request, 'question/answer.html', context=context)