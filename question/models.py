from django.db import models

# Create your models here.

class Question(models.Model):
    text = models.CharField(max_length=300)
    correct_answer = models.CharField(max_length=4)

class Answers(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    answer_option = models.CharField(max_length=4)
