# coding: utf8
from django.shortcuts import render
from django.views import View

from question.models import Question


class QuestionView(View):
    template_name = "question/question.html"
    answer_template_name = "question/answer.html"

    def get(self, request):
        context = {"question": Question.objects.first()}
        return render(request, self.template_name, context=context)

    def post(self, request):
        question_id = request.POST.get("question")
        question = Question.objects.get(id=question_id)
        answer = request.POST.get("answer", "z")
        is_correct = question.is_option_correct(answer)

        context = {
            "is_correct": is_correct,
        }

        return render(request, self.answer_template_name, context=context)
