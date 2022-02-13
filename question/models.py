from django.db import models

# Create your models here.

class Pergunta(models.Model):
    A = "A"
    B = "B"
    C = "C"
    D ="D"
    E ="E"
    
    CHOICES = (
        (A, "A"),
        (B, "B"),
        (C, "C"),
        (D, "D"),
        (E, "E")
    )
    

    texto = models.TextField('Texto da questão', null=True)
    opcao_A = models.CharField("Opção A", max_length=50, null=True)
    opcao_B = models.CharField("Opção B", max_length=50, null=True)
    opcao_C = models.CharField("Opção C", max_length=50, null=True)
    opcao_D = models.CharField("Opção D", max_length=50, null=True)
    opcao_E = models.CharField("Opção E", max_length=50, null=True)
    resposta =  models.CharField(
        u"Resposta", choices=CHOICES, max_length=20, blank=True, null=True
    )

    data_cadastro = models.DateTimeField(auto_now=True)
    #opcaos = models.ManyToManyField(Resposta)
    class Meta:
        verbose_name = "Pergunta"
        verbose_name_plural = "Perguntas"

    def __str__(self):
        return "%s" % (self.texto)