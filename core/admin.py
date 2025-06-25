from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Projeto

@admin.register(Projeto)
class ProjetoAdmin(ModelAdmin):
    list_display = ('titulo', 'link_github')