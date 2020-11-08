#coding: utf8
from django.shortcuts import render
from .models import Question, Response


def question(request):
    num_questions = Question.objects.count()

    if not num_questions:
        return render(request, 'question/no_question.html')

    # Verifica se existe parâmetro previous_question (questão anterior), caso contrário procura por primeiro.
    current_question_id = int(request.GET.get('current_question', 0))

    context = {
        'question': None
    }

    # Seegunda tentativa
    if current_question_id:
        question = Question.objects.get(id=current_question_id)
        context['question'] = question.to_dict()

        return render(request, 'question/question.html', context=context)

    previous_question_id = int(request.GET.get('previous_question', 0))

    question = Question.objects.filter(
        id__gt=previous_question_id if previous_question_id < num_questions else 0
    ).order_by('id').first()

    context['question'] = question.to_dict()

    return render(request, 'question/question.html', context=context)

def question_answer(request):

    answer = request.POST.get('answer', 'z')
    current_question = request.POST.get('current_question')
    question = Question.objects.get(id=current_question)
    is_correct = answer == question.correct_answer

    Response.objects.create(question=question, user_id=(request.session['user_id'] or None), answer=answer, is_correct=is_correct)

    context = {
        'is_correct': is_correct,
        'previous_question': current_question
    }

    return render(request, 'question/answer.html', context=context)
