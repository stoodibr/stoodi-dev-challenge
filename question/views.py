# coding: utf8
from django.shortcuts import render

from random import shuffle

from .models import Question, Answer


def question(request, template_name='question/pages/question.html'):
    question = Question.objects.first()

    answers = list(Answer.objects.filter(question__id=question.id))
    shuffle(answers)

    context = {
        'question': question,
        'answers': answers,
    }

    return render(request, template_name, context)


def question_answer(request, template_name='question/pages/answer.html'):
    answer = request.POST.get('answer', 'z')

    is_correct = Answer.objects.get(pk=answer).is_correct

    context = {
        'is_correct': is_correct,
    }

    return render(request, template_name, context)
