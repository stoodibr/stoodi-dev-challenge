from django.contrib import admin
from .models import Question, Answer


class ListQuestions(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_display_links = ('id', 'text')
    search_fields = ('id','text')

admin.site.register(Question, ListQuestions)

class ListAnswers(admin.ModelAdmin):
    list_display = ('id', 'text', 'question_id', 'is_correct')
    list_display_links = ('id', 'text')
    search_fields = ('id','text', 'question_id')

admin.site.register(Answer, ListAnswers)