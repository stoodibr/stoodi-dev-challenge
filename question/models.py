import uuid
from django.db import models



class Questao(models.Model):

    ALTERNATIVA_CHOICES = [
        ('a', 'Alternativa (A)'),
        ('b', 'Alternativa (B)'),
        ('c', 'Alternativa (C)'),
        ('d', 'Alternativa (D)'),
        ('e', 'Alternativa (E)'),
    ]

    identificador = models.UUIDField(
        'Identificador Unico', default=uuid.uuid4, unique=True, editable=False)

    numero = models.IntegerField('Número da questão', null=False, blank=False)

    enunciado = models.TextField(
        'Enunciado da questão',max_length=1000, null=False, blank=False)

    alternativa_a = models.CharField(
        verbose_name='Alternativa (A)', max_length=250, null=False, blank=False)
    alternativa_b = models.CharField(
        verbose_name='Alternativa (B)', max_length=250, null=False, blank=False)
    alternativa_c = models.CharField(
        verbose_name='Alternativa (C)', max_length=250, null=False, blank=False)
    alternativa_d = models.CharField(
        verbose_name='Alternativa (D)', max_length=250, null=False, blank=False)
    alternativa_e = models.CharField(
        verbose_name='Alternativa (E)', max_length=250, null=False, blank=False)


    alternativa_correta = models.CharField(
        max_length=1, choices=ALTERNATIVA_CHOICES, blank=False, null=False )

    ativa = models.BooleanField(
        help_text="A questão está ativa e visível?",
        default=True
    )

    class Meta:
        verbose_name = 'Questão'
        verbose_name_plural = 'Questões'
        ordering = ['numero']

    def __str__(self):
        return '{} - {}'.format(
            self.numero,
            self.enunciado
        )


class Resposta(models.Model):

    questao = models.ForeignKey(
        'Questao',
        related_name='log_respostas',
        null=True,
        on_delete=models.SET_NULL)
    data_resposta = models.DateTimeField(
        'Data de cadastro da resposta',
        null=True,
        blank=True,
        auto_now_add=True,
        editable=False)
    alternativa_escolhida = models.CharField(
        max_length=1, blank=False, null=False )
    alternativa_correta = models.BooleanField(
        help_text="A alternativa escolhida está correta?",
        default=False)
    
    class Meta:
        verbose_name = 'Resposta'
        verbose_name_plural = 'Respostas'
        ordering = ['data_resposta']

    def __str__(self):
        return '{}'.format(
            self.data_resposta
        )