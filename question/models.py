from collections import OrderedDict
from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.TextField(
        verbose_name="Questão",
        help_text="Enunciado da questão."
    )

    def add_answer(self, letter, value):
        Answer.objects.create(
            question=self,
            letter=letter,
            value=value
        )

    def get_answers(self):
        answers = {answer.letter:answer.value for answer in self.answers.all()}

        return OrderedDict(sorted(answers.items()))


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

