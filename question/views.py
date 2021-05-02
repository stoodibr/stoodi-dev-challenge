# coding: utf8
import collections
import logging

from django.shortcuts import render
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist

from question.models import Answer as AnswerModel, Question as QuestionModel


def log_config():
    logging.basicConfig(
        filename='answered_questions.log',
        format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        force=True
    )
    logger = logging.getLogger('answered_questions')
    logger.setLevel(level=logging.INFO)
    h = logging.StreamHandler()
    logger.addHandler(h)

    return logger


logger = log_config()


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
            try:
                correct_answer = AnswerModel.objects.filter(id=correct_answer_id).values()[0]
            except IndexError:
                raise ObjectDoesNotExist("This question does not have a correct answer")

            questions_list.append({
                'question_id': question.get('id'),
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
        question_id = question.object_list[0].get('question_id')
        correct_answer = question.object_list[0].get('correct_answer')

        is_correct = answer == correct_answer.get('choice_item')

        context = {
            'is_correct': is_correct,
            'question': question
        }

        logger.info({'question_id': question_id, 'answer_choice': answer, 'is_correct': is_correct})
        return render(request, 'question/answer.html', context=context)
