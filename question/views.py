#coding: utf8
from django.shortcuts import render

from .models import Question, Answer
from .utils.core import sort_dict_by_keys
from selecao.utils.database import queryset_to_dict
from .constants import QUESTION_TEMPLATE


def question(request):
    question = Question.objects.first()

    if question is None:
        return render(request, QUESTION_TEMPLATE)

    answers = (
        Answer.objects.filter(question=question.id)
        .order_by('letter').values()
    )

    answers_dict = (answers
                    and queryset_to_dict(answers, 'letter', 'text'))
    answers_sorted = answers_dict and sort_dict_by_keys(answers_dict)

    context = {
        'question_text': question.text,
        'answers': answers_sorted,
    }

    return render(request, QUESTION_TEMPLATE, context=context)


def question_answer(request):
    answer = request.POST.get('answer', 'z')
    is_correct = answer == 'd'

    context = {
        'is_correct': is_correct,
    }

    return render(request, 'question/answer.html', context=context)
