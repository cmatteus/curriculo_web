from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Projeto, Experiencia

@admin.register(Projeto)
class ProjetoAdmin(ModelAdmin):
    list_display = ('titulo', 'link_github')

@admin.register(Experiencia)
class ExperienciaAdmin(ModelAdmin):
    list_display = ('cargo', 'nome_empresa', 'data_inicio', 'data_fim', 'emprego_atual')