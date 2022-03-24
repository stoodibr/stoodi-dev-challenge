# coding: utf8
from curses.ascii import HT
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseNotFound, HttpResponseBadRequest

from question.models import Question


class QuestionView(View):
    template_name = "question/question.html"
    answer_template_name = "question/answer.html"

    def get(self, request, question_id=None):
        if question_id:
            try:
                question = Question.objects.get(id=question_id)
            except Question.DoesNotExist:
                return HttpResponseNotFound("Question does not exist.")
        else:
            questions = Question.objects.all()
            if questions.exists():
                question = questions.first()
            else:
                return HttpResponseNotFound(
                    "There are no questions on our database. Please contact an administrator."
                )
        context = {"question": question}
        return render(request, self.template_name, context=context)

    def post(self, request, question_id=None):
        if not question_id:
            question_id = request.POST.get("question_id")

        try:
            question = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            return HttpResponseNotFound("Question does not exist.")

        answer = request.POST.get("answer")
        try:
            is_correct = question.is_option_correct(answer)
        except KeyError:
            return HttpResponseBadRequest("The answer provided is not a valid option.")

        context = {
            "is_correct": is_correct,
            "current_question_id": question_id,
            "next_question_id": question.get_next_question_id(),
        }

        return render(request, self.answer_template_name, context=context)
