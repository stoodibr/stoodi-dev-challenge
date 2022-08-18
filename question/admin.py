from django.contrib import admin

from .models import Questao, Resposta


class QuestaoAdmin(admin.ModelAdmin):
    readonly_fields = ('identificador',)
    list_display = ('numero', 'enunciado', 'alternativa_correta','ativa')
    ordering = ('numero',)
    search_fields = ['numero', 'enunciado']
    

class RespostasAdmin(admin.ModelAdmin):

    list_display = ('data_resposta', 'questao', 'alternativa_escolhida', 'alternativa_correta')
    ordering = ('data_resposta',)
    
admin.site.register(Questao, QuestaoAdmin)
admin.site.register(Resposta, RespostasAdmin)
