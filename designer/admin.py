from django.contrib import admin
from designer.models import Designer , OpeningHour , ProjectImages , OfficeImages



class OpeningHourAdmin(admin.ModelAdmin):
    list_display = ('designer', 'day', 'from_hour', 'to_hour')


class DesignerAdmin(admin.ModelAdmin):
    list_display = ('user', 'designer_name', 'is_approved', 'created_at')
    list_display_links = ('user', 'designer_name')
    list_editable = ('is_approved',)
    




admin.site.register(Designer)
admin.site.register(OpeningHour, OpeningHourAdmin)
admin.site.register(ProjectImages)
admin.site.register(OfficeImages)




    

