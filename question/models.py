from django.db import models

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
    text = models.CharField(max_length=250, verbose_name='Resposta')
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, null=False)
    is_correct = models.BooleanField(choices=IS_CORRECT, default=False)
    
    class Meta:
        verbose_name = "Resposta"
        verbose_name_plural = "Respostas"
        ordering = ['id']

    def __str__(self):
        return self.text
