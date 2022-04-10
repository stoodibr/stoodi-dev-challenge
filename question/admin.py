from django.contrib import admin

from question.models import Answer, LogAnswers, Question

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(LogAnswers)