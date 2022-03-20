from django.db import models

from question.models import Question


class UserHistory(models.Model):
    question = models.ForeignKey(Question, on_delete=models.RESTRICT)
    letter = models.CharField(max_length=1)
    is_correct = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str({
            'question': self.question.id,
            'letter': self.letter,
            'is_correct': self.is_correct,
            'datetime': self.created_at
        })
