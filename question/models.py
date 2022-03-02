from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

IS_CORRECT = [(False,'Incorreta'),(True,'Correta')]

class Question(models.Model):
    text = models.CharField(max_length=250, verbose_name='Pergunta')
    
    class Meta:
        verbose_name = "Pergunta"
        verbose_name_plural = "Perguntas"
        ordering = ['id']

    def __str__(self):
        return self.text

class Answer(models.Model):
    """ This model saves the answer related to the Question Model """
    text = models.CharField(max_length=250, verbose_name='Resposta')
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, null=False)
    is_correct = models.BooleanField(choices=IS_CORRECT, default=False)
    
    class Meta:
        verbose_name = "Resposta"
        verbose_name_plural = "Respostas"
        ordering = ['id']

    def __str__(self):
        return self.text

class CustomLogQuestions(models.Model):
    """ This model saves as a 'log' the user selected answers """
    date = models.DateTimeField(default=timezone.now, verbose_name='Data resposta')
    selected_answer = models.CharField(max_length=255 , verbose_name='Alternativa escolhida')
    is_correct = models.CharField(max_length=255, verbose_name='Resposta')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Custom Log"
        verbose_name_plural = "Custom Logs"
        ordering = ['date']

    def __str__(self):
        user = self.user.first_name if self.user.first_name else self.user
        is_correct =  "Resposta Correta" if self.is_correct[0] == "T" else "Resposta Errada"
        return f"{self.date} - {user}  --  {self.selected_answer}  -- {is_correct}"



