from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.TextField(
        verbose_name="Questão",
        help_text="Enunciado da questão."
    )

class Answer(models.Model):
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

