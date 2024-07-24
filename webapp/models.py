from django.db import models

Variants  = [
      (1, 'Interior designer'),
      (2, 'Architect'),
      (3, 'Property '),
]
# Create your models here.
class Client(models.Model):
    client_photo = models.ImageField(upload_to='client_photos', blank=True, null=True)
    client_name = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.client_name
    


class Testimonial(models.Model):
    client_photo = models.ImageField(upload_to='client_photos', blank=True, null=True)
    client_name = models.CharField(max_length=250, blank=True, null=True)
    client_testimony = models.TextField(blank=True, null=True)
    client_category = models.IntegerField(choices=Variants)
    customer_name = models.CharField(max_length=250 , null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.client_name
    



class Ad_image(models.Model):
    Ad_photo = models.ImageField(upload_to='client_photos', blank=True, null=True)
    Ad_name = models.CharField(max_length=250, blank=True, null=True)
    

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.Ad_name
    

from django.db import models

# Create your models here.
class ContactDetails(models.Model):
    # location = 
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)


    def __str__(self):
        return str(self.id)