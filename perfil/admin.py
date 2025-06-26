from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import InformacaoPessoal, RedesSociais

@admin.register(InformacaoPessoal)
class InformacaoPessoalAdmin(ModelAdmin):
    list_display = ('nome_completo',)

@admin.register(RedesSociais)
class RedeSocialAdmin(ModelAdmin):
    list_display = ('linkedin', 'instagram', 'github')