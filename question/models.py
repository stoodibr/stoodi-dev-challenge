from django.db import models

# Models
class Question(models.Model):
    question_text = models.TextField(verbose_name="Questão")
    answer_date = models.DateField(null=True, blank=True)
    chosen_alternative = models.CharField(max_length=4, verbose_name="Alternativa", null=True, blank=True)
    is_correct = models.BooleanField(
        verbose_name="Está correta?", 
        default=False
    )
    
    def __str__(self):
        return self.question_text

    class Meta:
        ordering = ('pk',)
        verbose_name = 'Questão'
        verbose_name_plural = 'Questões'
        
class Alternatives(models.Model):
    alternative_order = models.CharField(max_length=4, verbose_name="Alternativa")
    question = models.ForeignKey(
        'Question', 
        on_delete=models.CASCADE, 
        verbose_name="Questão"
    )
    alternative_text = models.TextField(verbose_name="Questão")
    is_correct = models.BooleanField(
        verbose_name="Está correta?", 
        default=False
    )
    
    def __str__(self):
        return self.alternative_text

    class Meta:
        ordering = ('alternative_order',)
        verbose_name = 'Alternativa'
        verbose_name_plural = 'Alternativas'