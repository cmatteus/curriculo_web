from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Projeto, Experiencia, Formacao, Lingua, Educacao, Habilidade

@admin.register(Projeto)
class ProjetoAdmin(ModelAdmin):
    list_display = ('titulo', 'link_github')

@admin.register(Experiencia)
class ExperienciaAdmin(ModelAdmin):
    list_display = ('cargo', 'nome_empresa', 'data_inicio', 'data_fim', 'emprego_atual')

@admin.register(Lingua)
class LinguaAdmin(ModelAdmin):
    list_display = ('lingua', 'nivel')

@admin.register(Habilidade)
class HabilidadeAdmin(ModelAdmin):
    list_display = ('habilidade', 'tipo')


@admin.register(Educacao)
class EducacaoAdmin(ModelAdmin):
    list_display = ('titulo', 'instituicao', 'tipo', 'data_conclusao')


@admin.register(Formacao)
class FormacaoAdmin(ModelAdmin):
    list_display = ('curso', 'instituicao', 'grau', 'data_inicio', 'data_fim', 'em_andamento')