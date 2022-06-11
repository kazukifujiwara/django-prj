from django.contrib import admin
from .models import JsonData

@admin.register(JsonData)
class JsonDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'updated_at',)
    list_display_links = ('name', 'updated_at',)
    ordering = ('-updated_at',)