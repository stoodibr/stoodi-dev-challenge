from django.db import models


class Question(models.Model):
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} - {self.text}'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    letter = models.CharField(max_length=1)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Q{self.question.id}. ({self.letter}) {self.text}'
