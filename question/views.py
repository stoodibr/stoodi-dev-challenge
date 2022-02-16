# coding: utf8
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Question, Answer


def question(request, template_name='question/pages/question.html'):
    questions = Question.objects.all()
    paginator = Paginator(questions, 1)

    page_number = request.GET.get('question_id')
    questions_obj = paginator.get_page(page_number)

    context = {
        'questions_obj': questions_obj
    }

    return render(request, template_name, context)


def question_answer(request, template_name='question/pages/answer.html'):
    answer = request.POST.get('answer', 'z')
    page_number = request.POST['page_number']

    questions = Question.objects.all()
    paginator = Paginator(questions, 1)
    questions_obj = paginator.get_page(page_number)

    is_correct = Answer.objects.get(pk=answer).is_correct

    context = {
        'questions_obj': questions_obj,
        'is_correct': is_correct,
    }

    return render(request, template_name, context)
