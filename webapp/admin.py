from django.contrib import admin
from customers.models import Appointment , Checklist 
from .models import Client , Testimonial , Ad_image
 

# Register your models here.

admin.site.register(Appointment)
admin.site.register(Checklist)
admin.site.register(Client)
admin.site.register(Testimonial)
admin.site.register(Ad_image)



