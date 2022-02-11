# coding: utf8
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Question, Answer, QuestionAnswered


def question(request):
    answers = Answer.objects.all()

    context = {
        'answers': answers,
        'questions': questions_pagination(request),
    }

    return render(request, 'question/question.html', context=context)


def question_answer(request):
    answer = request.POST.get('answer', 'False').split(',')
    user_answer = answer[0]
    current_page = answer[1]

    is_correct = user_answer == 'True'

    context = {
        'is_correct': is_correct,
        'questions': question_answer_pagination(current_page)
    }

    save_answer(answer)

    return render(request, 'question/answer.html', context=context)


def questions_pagination(request):
    questions = Question.objects.all()
    paginator = Paginator(questions, 1)
    page = request.GET.get('question')
    questions = paginator.get_page(page)

    return questions


def question_answer_pagination(current_page):
    questions = Question.objects.all()
    paginator = Paginator(questions, 1)
    questions = paginator.get_page(current_page)

    return questions


def save_answer(answer):
    is_correct = answer[0]
    question_id = answer[2]
    answer_id = answer[3]

    QuestionAnswered.objects.create(
        question=Question.objects.get(id=question_id),
        answer=Answer.objects.get(id=answer_id),
        is_correct=is_correct)
