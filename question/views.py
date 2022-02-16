# coding: utf8
from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import Question, Answer, AnswerLog


def question(request, template_name='question/pages/question.html'):
    questions = Question.objects.all()
    paginator = Paginator(questions, 1)
    page_number = request.GET.get('question_id')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }

    return render(request, template_name, context)


def question_answer(request, template_name='question/pages/answer.html'):
    question = request.POST.get('question', 'z')
    answer = request.POST.get('answer', 'z')
    page_number = request.POST['page_number']

    questions = Question.objects.all()
    paginator = Paginator(questions, 1)
    page_obj = paginator.get_page(page_number)

    is_correct = Answer.objects.get(pk=answer).is_correct

    user = request.user if request.user.is_authenticated else None

    AnswerLog.objects.create(question_text=Question.objects.get(pk=question),
                             answer_text=Answer.objects.get(pk=answer).answer_text,
                             is_correct=is_correct,
                             user=user)

    context = {
        'page_obj': page_obj,
        'is_correct': is_correct,
    }

    return render(request, template_name, context)


@login_required(login_url="/login")
def answer_log(request, template_name='question/pages/answer_log.html'):
    logs = AnswerLog.objects.filter(user=request.user).order_by('created_at')

    context = {
        'logs': logs
    }

    return render(request, template_name, context)
