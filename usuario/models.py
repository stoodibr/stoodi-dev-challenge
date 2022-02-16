from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class Usuario(AbstractBaseUser):
    USERNAME_FIELD = 'email'

    nome = models.CharField((u'Nome'), max_length=100)
    email = models.EmailField(('Email'), unique=True, max_length=100, db_index=True)
    is_active = models.BooleanField((u'Ativo'), default=False, help_text='Se ativo o usuário tem permissão para acessar o sistema')

    class Meta:
        ordering            =   [u'nome']
        verbose_name        =   (u'usuário')
        verbose_name_plural =   (u'usuários')

    def __str__(self):
        return '%s - %s ' % (self.nome, self.email)