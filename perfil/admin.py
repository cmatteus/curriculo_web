from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import InformacaoPessoal

@admin.register(InformacaoPessoal)
class InformacaoPessoalAdmin(ModelAdmin):
    list_display = ('nome_completo',)