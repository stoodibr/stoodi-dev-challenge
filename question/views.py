#coding: utf8
import collections

from django.shortcuts import render
from django.core.paginator import Paginator

from question.models import Answer as AnswerModel, Question as QuestionModel


class Question:

    def __init__(self):
        self.set_questions_list()


    def set_questions_list(self):
        q = QuestionModel.objects.all().values()

        questions_list = []
        for question in q:
            a = AnswerModel.objects.filter(question_ref=question.get('id')).values()
            answers = {}
            for answer in a:
                answers.update({answer['choice_item']: answer['response']})
            sorted_answers = collections.OrderedDict(sorted(answers.items()))

            correct_answer_id = question.get('correct_answer_id')
            correct_answer = AnswerModel.objects.filter(id=correct_answer_id).values()[0]

            questions_list.append({
                'question_text': question.get('text'),
                'correct_answer': correct_answer,
                'answers': sorted_answers,
            })
        
        self.paginator = Paginator(questions_list, 1)


    def question(self, request):
        self.page = request.GET.get('page') or 1
        question = self.paginator.get_page(self.page)

        context = {
            'page': self.page,
            'question': question
        }

        return render(request, 'question/question.html', context=context)


    def question_answer(self, request):
        answer = request.POST.get('answer', 'z')
        question = self.paginator.get_page(self.page)
        correct_answer = question.object_list[0].get('correct_answer')

        is_correct = answer == correct_answer.get('choice_item')

        context = {
            'is_correct': is_correct,
            'question': question
        }

        return render(request, 'question/answer.html', context=context)
