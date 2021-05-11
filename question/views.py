import logging
from django.shortcuts import render
from django.core.paginator import Paginator
from collections import OrderedDict

from .models import Question


class LogQuestion:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.formatter = logging.Formatter('%(asctime)s:%(message)s', "%Y-%m-%d %H:%M:%S")
        self.file_handler = logging.FileHandler('logs/questions.log')
        self.file_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.file_handler)

    def _remove_all_handlers(self):
        self.logger.handlers = []

    def set_user_log(self, user):
        self._remove_all_handlers()
        file_handler = logging.FileHandler(f'logs/{user}-questions.log')
        file_handler.setFormatter(self.formatter)
        self.logger.addHandler(file_handler)

    def set_no_user_log(self):
        self._remove_all_handlers()
        self.file_handler = logging.FileHandler('logs/questions.log')
        self.file_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.file_handler)


class QuestionView:
    def __init__(self):
        self.all_questions = Question.objects.all().order_by('id')
        self.paginator = Paginator(self.all_questions, 1)
        self.page_num = 0
        self.page = None
        self.log = LogQuestion()

    def question(self, request):
        if len(self.all_questions) == 0:
            return render(request, 'question/no_question.html')
        self.page_num = request.GET.get('page') or 1
        self.page = self.paginator.get_page(self.page_num)
        text = self.all_questions[int(self.page_num) - 1]
        answers = self.all_questions[int(self.page_num) - 1].get_answers()
        context = {
            'question_text': text,
            'answers': OrderedDict(sorted(answers.items())),
            'page': self.page,
        }
        return render(request, 'question/question.html', context=context)

    def question_answer(self, request):
        answer = request.POST.get('answer', 'z')
        question = self.all_questions[int(self.page_num) - 1]
        is_correct = answer == question.correct_answer.letter
        context = {
            'is_correct': is_correct,
            'page': self.page
        }
        user = request.user.username
        if user:
            self.log.set_user_log(user)
            self.log.logger.info(
                {'user': user,
                 'question_number': str(self.page_num),
                 'chosen-answer': answer,
                 'is_correct': is_correct})
        else:
            self.log.set_no_user_log()
            self.log.logger.info(
                {'user': None,
                 'question_number': str(self.page_num),
                 'chosen-answer': answer,
                 'is_correct': is_correct})
        return render(request, 'question/answer.html', context=context)
