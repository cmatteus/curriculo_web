from django.contrib import admin
from unfold.admin import ModelAdmin

@admin.register(ModelAdmin)
class CustomAdminClass(ModelAdmin):
    pass
