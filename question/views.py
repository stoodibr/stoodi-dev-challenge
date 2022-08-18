#coding: utf8
from django.shortcuts import render, redirect
from .models import Question, Alternatives, QuestionLogs
import datetime

def home(request):
    questions = Question.objects.all().first()
    
    if questions:
        return redirect('question', questions.id)
    else:
        context = {}
        return render(request, 'question/question.html', context=context)

def question(request, id):
    questions = Question.objects.get(id=id)
    
    context = {
        "questions":{},
        }
    
    if questions:
        alternatives = Alternatives.objects.filter(question__id=id)
        context['questions'] = {
                                    "question_complete":questions,
                                    "question":questions.question_text,
                                    "alternatives":alternatives
                                }
        
    return render(request, 'question/question.html', context=context)
    
def question_answer(request):
    questions = Question.objects.all()
    try:
        answer_id = request.POST.get('answer')
        
        alternative = Alternatives.objects.get(id=answer_id)

        context = {
            'is_correct': alternative.is_correct,
            'id': alternative.question.id,
            'user_logged': request.user.is_authenticated
        }
        
        if alternative.question.id < len(questions):
            context['next'] = alternative.question.id + 1
        else:
            questions = Question.objects.all().first()
            context['next'] = questions.id
        
        question = Question.objects.get(id=alternative.question.id)
        
        if request.user.is_authenticated:
            QuestionLogs.objects.create(
                user = request.user,
                question = question,
                chosen_alternative = alternative.alternative_order,
                is_correct = alternative.is_correct,
                answer_date = datetime.date.today()
            )
        else:
            QuestionLogs.objects.create(
                question = question,
                chosen_alternative = alternative.alternative_order,
                is_correct = alternative.is_correct,
                answer_date = datetime.date.today()
            )
        
        return render(request, 'question/answer.html', context=context)
    except:
        return redirect('question_home')

def logs(request):
    
    if request.user.is_authenticated:
        logs = QuestionLogs.objects.filter(user=request.user)
        
        context = {
                'user': request.user,
                'logs': logs
            }
        
        return render(request, 'question/question_logs.html', context=context)
    else:
        return redirect('question_home')