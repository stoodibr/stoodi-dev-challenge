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
    correct_answer = models.ForeignKey(
        'question.Answer',
        related_name='correct_answer',
        null=True,
        on_delete=models.PROTECT
    )

    def add_answer(self, letter, value):
        Answer.objects.create(
            question=self,
            letter=letter,
            text=value
        )

    def set_correct_answer(self, letter):
        self.correct_answer = Answer.objects.get(question=self, letter=letter)
        self.save()

    def get_answers(self):
        answers = {answer.letter:answer.text for answer in self.answers.all()}

        return OrderedDict(sorted(answers.items()))

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'answers': self.get_answers(),
            'correct_answer': self.correct_answer.letter
        }


class Answer(models.Model):
    class Meta:
        unique_together = ('question_id', 'letter')

    question = models.ForeignKey(
        'question.Question',
        related_name='answers',
        on_delete=models.CASCADE
    )
    letter = models.CharField(
        max_length=1,
        verbose_name='Opção (letra)'
    )
    text = models.TextField(
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
        on_delete=models.CASCADE
    )
    answer = models.ForeignKey(
        'question.Answer',
        on_delete=models.PROTECT
    )


    @property
    def is_correct(self):
        return self.answer == self.question.correct_answer

    def to_dict(self):
        return {
            'question_id': self.question.id,
            'answer': self.answer,
            'is_correct': 'Sim' if self.is_correct else 'Não',
            'answered_at': self.answered_at.strftime("%d/%m/%Y - %H:%M:%S")
        }
