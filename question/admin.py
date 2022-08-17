from django.contrib import admin
from .models import Question, Alternatives

# Register admin models
admin.site.register(Question)

@admin.register(Alternatives)
class alternativesAdmin(admin.ModelAdmin):
    list_display = (
        'alternative_order',
        'question',
        'alternative_text',
        'is_correct'
    )