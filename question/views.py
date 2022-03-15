#coding: utf8
from django.shortcuts import render
from utils.sort import sorting_answers

from .models import Question, Answers


def question(request):
    questions = Question.objects.order_by('id')
    for question in questions:
        text = question.text
        answers_list = {
            'a': question.choice_a,
            'b': question.choice_b,
            'c': question.choice_c,
            'd': question.choice_d,
            'e': question.choice_e,
        }
        question_id = question.id
   
    context = {
        'text': text,
        'answers_list': sorting_answers(answers_list),
        'question_id': question_id
    }

    return render(request, 'question/question.html', context=context)

def question_answer(request):
    answer = request.POST.get('answer', 'z')
    question_id = request.POST.get('question_id', '1')
    is_correct = answer == Question.objects.get(id=question_id).correct_answer

    context = {
        'is_correct': is_correct,
    }

    return render(request, 'question/answer.html', context=context)