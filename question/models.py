from django.db import models
from django.utils import timezone


class Question(models.Model):
    text = models.TextField()
    correct_answer = models.OneToOneField('question.QuestionChoice', on_delete=models.CASCADE, related_name="answers_question", null=True)


class QuestionChoice(models.Model):
    question = models.ForeignKey('question.Question', on_delete=models.CASCADE, related_name='answers')
    text = models.TextField()
    label = models.CharField(max_length=1)


class QuestionRecords(models.Model):
    question = models.ForeignKey('question.Question', on_delete=models.CASCADE, related_name='records')
    created_at = models.DateTimeField()
    answered = models.CharField(max_length=1)
    is_correct_answered = models.BooleanField()

    def save(self, *args, **kwargs):
        self.created_at = timezone.now()
        self.is_correct_answered = self.question.correct_answer.label == self.answered.upper()
        super(QuestionRecords, self).save(*args, **kwargs)