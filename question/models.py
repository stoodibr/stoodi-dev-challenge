from django.db import models


class Question(models.Model):
    text = models.CharField(max_length=100)
    correct_answer = models.ForeignKey('Answer', on_delete=models.CASCADE)


class Answer(models.Model):
    question_ref = models.ForeignKey('Question', on_delete=models.CASCADE)
    choice_item = models.CharField(max_length=1)
    response = models.CharField(max_length=100)
