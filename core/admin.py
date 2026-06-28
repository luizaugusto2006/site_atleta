from django.contrib import admin
from .models import Atleta, Foto, HistoricoClube

class FotoInline(admin.TabularInline):
    model = Foto
    extra = 3
    fields = ['imagem', 'legenda']

class HistoricoClubeInline(admin.TabularInline):
    model = HistoricoClube
    extra = 1
    fields = ['nome_clube', 'ano_inicio', 'ano_fim', 'conquistas']

@admin.register(Atleta)
class AtletaAdmin(admin.ModelAdmin):
    list_display = ['nome_artistico', 'get_posicao_display', 'data_nascimento', 'altura', 'instagram']
    list_filter = ['posicao', 'pe_dominante']
    search_fields = ['nome_artistico', 'instagram']
    fieldsets = [
        ('Informações Principais', {
            'fields': ['nome_artistico', 'foto_rosto', 'posicao']
        }),
        ('Dados Pessoais', {
            'fields': ['data_nascimento', 'altura', 'pe_dominante']
        }),
        ('Contato e Redes', {
            'fields': ['instagram', 'whatsapp', 'link_video']
        }),
        ('Habilidades Técnicas', {
            'fields': ['visao_jogo', 'precisao_passe', 'controle_bola']
        }),
    ]
    inlines = [FotoInline, HistoricoClubeInline]

@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):
    list_display = ['legenda', 'atleta', 'imagem']
    list_filter = ['atleta']

@admin.register(HistoricoClube)
class HistoricoClubeAdmin(admin.ModelAdmin):
    list_display = ['nome_clube', 'ano_inicio', 'ano_fim', 'conquistas', 'atleta']
    list_filter = ['atleta']
    search_fields = ['nome_clube', 'conquistas']