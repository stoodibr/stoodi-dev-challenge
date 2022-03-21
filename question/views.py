#coding: utf8
from django.shortcuts import render

from selecao.utils.database import queryset_to_dict
from question.models import Question, Answer
from question.utils.core import sort_dict_by_keys
from question.utils.answer import check_answer
from question.constants import QUESTION_TEMPLATE, ANSWER_TEMPLATE
from user.models import UserHistory


def question(request):
    last_question = Question.objects.last()

    if not(last_question):
        return render(request, QUESTION_TEMPLATE)

    question_id = request.GET.get('q')

    if not(question_id) or int(question_id) > last_question.id:
        question_id = Question.objects.first().id

    question = Question.objects.get(id=question_id)

    answers = (
        Answer.objects.filter(question=question.id)
        .order_by('letter')
        .values()
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
        question = question_id and Question.objects.get(id=question_id)
        total_questions = Question.objects.count()

        is_correct = check_answer(question_id, answer)

        user = request.user if request.user.is_authenticated else None
    except Exception:
        context['success'] = False

    else:
        context['is_correct'] = is_correct
        context['total_questions'] = total_questions
        context['question_id'] = question_id

        UserHistory(
            question=question,
            letter=answer,
            is_correct=is_correct,
            user=user
        ).save()

    finally:
        return render(request, ANSWER_TEMPLATE, context=context)
