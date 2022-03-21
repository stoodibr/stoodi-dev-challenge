from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models

from question.models import Question
from user.managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class UserHistory(models.Model):
    question = models.ForeignKey(Question, on_delete=models.RESTRICT)
    letter = models.CharField(max_length=1)
    is_correct = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str({
            'user': self.user,
            'question': self.question.id,
            'letter': self.letter,
            'is_correct': self.is_correct,
            'datetime': self.created_at
        })
