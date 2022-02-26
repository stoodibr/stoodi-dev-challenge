#coding: utf8
from django.shortcuts import render
from .models import Question, Answer
from .classes.questions_class import *

# class QuestionsRequest():

#     def __init__(self, id = None):
#         self.__context = self.__get_questions_context(id)

#     def __get_questions_context(self, id_question):

#         question = Question.objects.get(id=id_question) if id_question else Question.objects.all()[0]
#         answer_list = Answer.objects.filter(question_id=question.id)[:5]
    
#         if answer_list:
#             return {
#                 'question_text': question.text,
#                 'answers': answer_list,
#             }
        
#         raise ValueError('A pergunta solicitada ainda não está disponível')
    
#     def get_context(self):

#         return self.__context

def question(request, id = None):

    try:
        context = QuestionsRequest(id).get_context()

    except Exception as e:
        context = {
            'error_msg' : str(e)
        }

    return render(request, 'question/question.html', context=context)

def question_answer(request):
    
    answer, is_correct = request.POST.get('answer', None), False
    
    if answer:
        is_correct = Answer.objects.get(id=answer).is_correct

    context = {
        'is_correct': is_correct,
    }

    return render(request, 'question/answer.html', context=context)


# def question(request):
   
#     context = QuestionsRequest().get_context()
#     context['teste'] = request.GET.get('id', 'errow')

#     return render(request, 'question/question.html', context=context)

# def question_answer(request):
#     answer = request.POST.get('answer', 'z')
#     is_correct = answer == 'd'

#     context = {
#         'is_correct': is_correct,
#     }

#     return render(request, 'question/answer.html', context=context)