from django.contrib import admin

from .models import Question, Answer


admin.site.register([Question, Answer])
