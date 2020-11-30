from collections import OrderedDict
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.TextField(
        verbose_name="Questão",
        help_text="Enunciado da questão.",
        max_length=3000
    )
    correct_answer = models.CharField(
        max_length=1,
        null=True
    )

    def add_answer(self, letter, value):
        Answer.objects.create(
            question=self,
            letter=letter,
            value=value
        )

    def set_correct_answer(self, letter):
        self.correct_answer = letter
        self.save()

    def get_answers(self):
        answers = {answer.letter:answer.value for answer in self.answers.all()}

        return OrderedDict(sorted(answers.items()))

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'answers': self.get_answers(),
            'correct_answer': self.correct_answer
        }


class Answer(models.Model):
    class Meta:
        unique_together = ('question_id', 'letter')

    question = models.ForeignKey(
        'question.Question',
        related_name='answers',
        on_delete = models.CASCADE
    )
    letter = models.CharField(
        max_length=1,
        verbose_name='Opção (letra)'
    )
    value = models.TextField(
        verbose_name='Texto da resposta'
    )


class Response(models.Model):
    answered_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL)
    question = models.ForeignKey(
        'question.Question',
        related_name='responses',
        on_delete = models.CASCADE
    )
    answer = models.CharField(
        max_length=1
    )
    is_correct = models.BooleanField()

    def to_dict(self):
        return {
            'question_id': self.question.id,
            'answer': self.answer,
            'is_correct': 'Sim' if self.is_correct else 'Não',
            'answered_at': self.answered_at.strftime("%d/%m/%Y - %H:%M:%S")
        }
