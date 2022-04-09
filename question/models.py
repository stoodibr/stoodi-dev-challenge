from django.db import models

class Question(models.Model):
    description = models.TextField()
    correct_alternative = models.CharField(max_length=1)

    def __str__(self):
        return self.description

class Answer(models.Model): 
    alternative = models.CharField(max_length=1)
    description = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

