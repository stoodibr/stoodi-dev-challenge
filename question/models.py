from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name="Texto da pergunta")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200, verbose_name="Resposta")
    is_correct = models.BooleanField(default=False, verbose_name="Essa é a resposta correta?")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Pergunta: {self.question} / Alternativa: {self.answer_text} / {self.is_correct}'


class AnswerLog(models.Model):
    question_text = models.CharField(max_length=200)
    answer_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    user = models.CharField(max_length=50, default='Anônimo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Pergunta: {self.question_text} Resposta: {self.answer_text}'
