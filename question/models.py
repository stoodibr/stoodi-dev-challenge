from datetime import datetime
from django.db import models

# Create your models here.

class Question(models.Model):
    text = models.CharField(max_length=400)
    choice_a = models.CharField(max_length=4, null=True)
    choice_b = models.CharField(max_length=4, null=True)
    choice_c = models.CharField(max_length=4, null=True)
    choice_d = models.CharField(max_length=4, null=True)
    choice_e = models.CharField(max_length=4, null=True)

    correct_answer = models.CharField(max_length=4, null=True)

class Answers(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_option = models.CharField(max_length=4)
    date = models.DateField('reply date', default=datetime.now)
    is_correct = models.BooleanField('is the answer correct', default= True)
