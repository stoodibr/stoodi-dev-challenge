from django.contrib import admin
from .models import Question, Alternatives, QuestionLogs

# Register admin models
admin.site.register(Question)

@admin.register(Alternatives)
class AlternativesAdmin(admin.ModelAdmin):
    list_display = (
        'alternative_order',
        'question',
        'alternative_text',
        'is_correct'
    )
    
@admin.register(QuestionLogs)
class QuestionLogsAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'question',
        'chosen_alternative',
        'is_correct',
        'answer_date'
    )