#coding: utf8
from django.shortcuts import render
from .models import Question, Alternatives

def question(request):
    questions = Question.objects.all()
    
    context = {
        "questions":[]
        }
    
    for question in questions:
        alternatives = Alternatives.objects.filter(question=question)
        context['questions'].append(
            {
                "question":question,
                "alternatives":alternatives
            }
        )

    return render(request, 'question/question.html', context=context)

def question_answer(request):
    answer = request.POST.get('answer', 'z')
    is_correct = answer == 'd'

    context = {
        'is_correct': is_correct,
    }

    return render(request, 'question/answer.html', context=context)