from django.contrib import admin
from .models import Builder , Builder_OpeningHour , Builder_OfficeImages , Builder_ProjectImages



class Builder_OpeningHourAdmin(admin.ModelAdmin):
    list_display = ('builder', 'day', 'from_hour', 'to_hour')


class BuilderAdmin(admin.ModelAdmin):
    list_display = ('user', 'builder_name', 'is_approved', 'created_at')
    list_display_links = ('user', 'builder_name')
    list_editable = ('is_approved',)
    




admin.site.register(Builder)
admin.site.register(Builder_OpeningHour, Builder_OpeningHourAdmin)
admin.site.register(Builder_ProjectImages)
admin.site.register(Builder_OfficeImages)




    

