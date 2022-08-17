from django.contrib import admin

from .models import Questao


class QuestaoAdmin(admin.ModelAdmin):
    readonly_fields = ('identificador',)
    list_display = ('numero', 'enunciado', 'alternativa_correta','ativa')
    ordering = ('numero',)
    search_fields = ['numero', 'enunciado']
    

admin.site.register(Questao, QuestaoAdmin)
