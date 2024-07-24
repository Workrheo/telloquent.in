from django.contrib import admin
from .models import Architect , Architect_OpeningHour , Architect_OfficeImages , Architect_ProjectImages



class Architect_OpeningHourAdmin(admin.ModelAdmin):
    list_display = ('architect', 'day', 'from_hour', 'to_hour')


class ArchitectAdmin(admin.ModelAdmin):
    list_display = ('user', 'architect_name', 'is_approved', 'created_at')
    list_display_links = ('user', 'architect_name')
    list_editable = ('is_approved',)
    




admin.site.register(Architect)
admin.site.register(Architect_OpeningHour, Architect_OpeningHourAdmin)
admin.site.register(Architect_ProjectImages)
admin.site.register(Architect_OfficeImages)




    

