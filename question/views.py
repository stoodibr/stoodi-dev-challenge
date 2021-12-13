#coding: utf8
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import Question, QuestionRecords
from .serializers import QuestionCreateSerializer, QuestionRetrieveSerializer

import pdb


def question(request, id="1"):
    
    data_list = Question.objects.all().filter(id__gte=id).order_by("id")
    data = data_list.first()

    if len(data_list) > 1:
        next_id = data_list[1].id
    else:
        next_id = Question.objects.all().order_by("id").first().id
    
    question = QuestionRetrieveSerializer(data)
    answers = {}

    for answer in question.data["answers"]:
        answers[answer["label"].lower()] = answer["text"]

    context = {
        'question_text': question.data["text"],
        'answers': answers,
        'id': data.id,
        'next_id': str(next_id) if next_id != id else None
    }

    return render(request, 'question/question.html', context=context)


def question_answer(request, id):
    answer = request.POST.get('answer', 'z')
    question = Question.objects.get(id=id)
    is_correct = answer == question.correct_answer.label.lower()

    QuestionRecords.objects.create(question=question, answered=answer)

    context = {
        'is_correct': is_correct,
    }

    return render(request, 'question/answer.html', context=context)


class QuestionCreateView(GenericAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionCreateSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_question = serializer.create(serializer.data)

        question = Question.objects.get(id=new_question.id)
        pdb.set_trace()

        new_question = QuestionRetrieveSerializer(question)
        return Response(new_question.data, status=status.HTTP_201_CREATED)