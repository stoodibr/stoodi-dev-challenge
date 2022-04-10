from django.contrib import admin

from question.models import Answer, Question

admin.site.register(Question)
admin.site.register(Answer)