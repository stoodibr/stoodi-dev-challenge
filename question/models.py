from django.db import models

# Create your models here.
class Question(models.Model):
    text = models.TextField()
    correct_answer = models.OneToOneField('question.QuestionChoice', on_delete=models.CASCADE, related_name="answers_question", null=True)


class QuestionChoice(models.Model):
    question = models.ForeignKey('question.Question', on_delete=models.CASCADE, related_name='answers')
    text = models.TextField()
    label = models.CharField(max_length=1)