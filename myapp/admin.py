from django.contrib import admin
from .models import Hostname, GetInterfaces

    
@admin.register(Hostname)
class HostnameAdmin(admin.ModelAdmin):
    list_display = ('hostname',)
    list_display_links = ('hostname',)
    ordering = ('hostname',)
    
@admin.register(GetInterfaces)
class GetInterfacesAdmin(admin.ModelAdmin):
    list_display = ('hostname', 'updated_at',)
    list_display_links = ('hostname', 'updated_at',)
    ordering = ('-updated_at',)
