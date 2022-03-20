#coding: utf8
from django.shortcuts import render

from selecao.utils.database import queryset_to_dict
from question.models import Question, Answer
from question.utils.core import sort_dict_by_keys
from question.utils.answer import check_answer
from question.constants import QUESTION_TEMPLATE, ANSWER_TEMPLATE


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
        'question_id': question.id,
        'question_text': question.text,
        'answers': answers_sorted,
    }

    return render(request, QUESTION_TEMPLATE, context=context)


def question_answer(request):
    context = {
        'success': True
    }

    try:
        answer = request.POST.get('answer', 'z')
        question_id = request.POST.get('question_id')

        is_correct = check_answer(question_id, answer)

    except:
        context['success'] = False

    else:
        context['is_correct'] = is_correct

    finally:
        return render(request, ANSWER_TEMPLATE, context=context)
