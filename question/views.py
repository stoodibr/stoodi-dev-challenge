#coding: utf8
from django.shortcuts import render, redirect
from .models import Question, Alternatives, QuestionLogs
import datetime

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
            'id': alternative.question.id
        }
        
        if alternative.question.id < len(questions):
            context['next'] = alternative.question.id + 1
        else:
            context['next'] = 1
        
        question = Question.objects.get(id=alternative.question.id)
        
        QuestionLogs.objects.create(
            question = question,
            chosen_alternative = alternative.alternative_order,
            is_correct = alternative.is_correct,
            answer_date = datetime.date.today()
        )
        
        return render(request, 'question/answer.html', context=context)
    except:
        return redirect('question', id=1)
    
