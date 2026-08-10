from django.contrib import admin
from .models import Atleta, Foto, HistoricoClube, Estatistica, Depoimento

class FotoInline(admin.TabularInline):
    model = Foto
    extra = 3
    fields = ['imagem', 'legenda']

class HistoricoClubeInline(admin.TabularInline):
    model = HistoricoClube
    extra = 1
    fields = ['nome_clube', 'ano_inicio', 'ano_fim', 'conquistas']

class EstatisticaInline(admin.TabularInline):
    model = Estatistica
    extra = 1
    fields = ['temporada', 'gols', 'assistencias', 'jogos', 'minutos', 'cartoes_amarelos', 'cartoes_vermelhos']

class DepoimentoInline(admin.TabularInline):
    model = Depoimento
    extra = 1
    fields = ['autor', 'cargo', 'texto', 'foto']

@admin.register(Atleta)
class AtletaAdmin(admin.ModelAdmin):
    list_display = ['nome_artistico', 'get_posicao_display', 'data_nascimento', 'altura', 'instagram']
    list_filter = ['posicao', 'pe_dominante']
    search_fields = ['nome_artistico', 'instagram']
    fieldsets = [
        ('Informações Principais', {
            'fields': ['nome_artistico', 'foto_rosto', 'foto_capa', 'posicao']
        }),
        ('Dados Pessoais', {
            'fields': ['data_nascimento', 'altura', 'pe_dominante']
        }),
        ('Contato e Redes', {
            'fields': ['instagram', 'whatsapp', 'link_video']
        }),
        ('Sobre Mim', {
            'fields': ['sobre_mim']
        }),
        ('Habilidades Técnicas', {
            'classes': ('collapse',),
            'fields': ['visao_jogo', 'precisao_passe', 'controle_bola', 'velocidade', 'dribles', 'finalizacao', 'defesa', 'fisico', 'disputa_aerea', 'cavarinha']
        }),
    ]
    inlines = [EstatisticaInline, FotoInline, HistoricoClubeInline, DepoimentoInline]

@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):
    list_display = ['legenda', 'atleta', 'imagem']
    list_filter = ['atleta']

@admin.register(HistoricoClube)
class HistoricoClubeAdmin(admin.ModelAdmin):
    list_display = ['nome_clube', 'ano_inicio', 'ano_fim', 'conquistas', 'atleta']
    list_filter = ['atleta']
    search_fields = ['nome_clube', 'conquistas']

@admin.register(Estatistica)
class EstatisticaAdmin(admin.ModelAdmin):
    list_display = ['temporada', 'atleta', 'gols', 'assistencias', 'jogos', 'minutos']
    list_filter = ['temporada', 'atleta']

@admin.register(Depoimento)
class DepoimentoAdmin(admin.ModelAdmin):
    list_display = ['autor', 'cargo', 'atleta']
    list_filter = ['atleta']
    search_fields = ['autor', 'texto']
