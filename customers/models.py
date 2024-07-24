from django.db import models
from accounts.models import User, UserProfile
from datetime import time, date, datetime


class Appointment(models.Model):
   designer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='designer_appointments')
   customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_appointments')
   a_date = models.DateField(null=True)
   a_timing = models.TimeField(null=True)
   status = models.CharField(max_length=100, null=True)
   c_status = models.CharField(max_length=100, null=True)
   
   def __str__(self):
        return f"{self.designer.username} - {self.customer.username}"
   

class Architect_Appointment(models.Model):
   architect = models.ForeignKey(User, on_delete=models.CASCADE, related_name='architect_appointments')
   customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_arc_appointments')
   a_date = models.DateField(null=True)
   a_timing = models.TimeField(null=True)
   status = models.CharField(max_length=100, null=True)
   c_status = models.CharField(max_length=100, null=True)
   
   def __str__(self):
        return f"{self.architect.username} - {self.customer.username}"
   

class Builder_Appointment(models.Model):
   builder = models.ForeignKey(User, on_delete=models.CASCADE, related_name='builder_appointments')
   customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_builder_appointments')
   a_date = models.DateField(null=True)
   a_timing = models.TimeField(null=True)
   status = models.CharField(max_length=100, null=True)
   c_status = models.CharField(max_length=100, null=True)
   
   def __str__(self):
        return f"{self.architect.username} - {self.customer.username}"
   

class Checklist(models.Model):
   k_finishes = [
      (1 , 'Laminate_Glossy'),
      (2 , 'Laminate_Matt'),
      (3 , 'Acrylic'),
      (4 , 'PU/DUCO'),
      (5 , 'Laminate_Glossy and Laminate_Matt'),
      (6 , 'Laminate_Glossy and Acrylic'),
      (7 , 'Acrylic and PU/DUCO'),
      (8, 'NA'),

   ]

   k_countertop = [
      (1, 'Grantite'),
      (2, 'Quartz'),
      (3, 'NA'),


   ]
   
   k_dado = [
      (1, 'Tiles'),
      (2, 'Quartz'),
      (3, 'NA'),



   ]

   k_loft = [
      (1, 'REQUIRED'),
      (2, 'NOT REQUIRED'),
   ]

   type = [
      (1, '1BHK Apartment'),
      (2, '2BHK Apartment'),
      (3, '3BHK Apartment'),
      (4, '4BHK Apartment'),
      (5, '5BHK Apartment'),
      (6, 'Villa'),
      (7, 'Individual Apartment'),
   ]

   category = [
      (1, 'New home interiors'),
      (2, 'Renovation interiors'),
   ]


   utilities = [
      (1, 'Wall unit'),
      (2, 'Base unit'),
      (3, 'Both Base and Wall unit'),
      (4, 'NA'),



   ]

   MBR_Wardrobe = [
      (1, 'Sliding Wardrobe'),
      (2, 'Openable Wardrobe'),
      (3, 'Sliding Wardrobe with Loft'),
      (4, 'Openable Wardrobe with Loft'),
      (5, 'NA'),

   ]

   MBR_COT =  [
      (1, 'King Size'),
      (2, 'Queen Size'),
      (3, 'NA'),
   ]

   MBR_Reqs = [
      (1, 'Chest Of Drawer'),
      (2, 'Dresser'),
      (3, 'Bay Window'),
      (4, 'Dresser ,  Chest Of Drawer'),
      (5, 'Bay window ,Chest Of Drawer ,Dresser and Study'),
      (6, 'Bay window ,  Dresser ,  Study , Wallpaper'),
      (7, 'Bay window ,  Dresser ,  Study , Wallpaper, Painting'),
      (8, 'NA'),

   ]


   KBR_Wardrobe = [
      (1, 'Sliding Wardrobe'),
      (2, 'Openable Wardrobe'),
      (3, 'Sliding Wardrobe with Loft'),
      (4, 'Openable Wardrobe with Loft'),
      (5, 'NA'),

   ]

   KBR_COT =  [
      (1, 'King Size'),
      (2, 'Queen Size'),
      (3, 'NA'),
   ]

   KBR_Reqs = [
      (1, 'Chest Of Drawer'),
      (2, 'Dresser'),
      (3, 'Bay Window'),
      (4, 'Dresser ,  Chest Of Drawer'),
      (5, 'Bay window ,Chest Of Drawer ,Dresser and Study'),
      (6, 'Bay window ,  Dresser ,  Study , Wallpaper'),
      (7, 'Bay window ,  Dresser ,  Study , Wallpaper, Painting'),
      (8, 'NA'),

   ]


   GBR_Wardrobe = [
      (1, 'Sliding Wardrobe'),
      (2, 'Openable Wardrobe'),
      (3, 'Sliding Wardrobe with Loft'),
      (4, 'Openable Wardrobe with Loft'),
      (5, 'NA'),

   ]

   GBR_COT =  [
      (1, 'King Size'),
      (2, 'Queen Size'),
      (3, 'NA'),
   ]

   GBR_Reqs = [
      (1, 'Chest Of Drawer'),
      (2, 'Dresser'),
      (3, 'Bay Window'),
      (4, 'Dresser ,  Chest Of Drawer'),
      (5, 'Bay window ,Chest Of Drawer ,Dresser and Study'),
      (6, 'Bay window ,  Dresser ,  Study , Wallpaper'),
      (7, 'Bay window ,  Dresser ,  Study , Wallpaper, Painting'),
      (8, 'NA'),

   ]

   KBR_Wardrobe = [
      (1, 'Sliding Wardrobe'),
      (2, 'Openable Wardrobe'),
      (3, 'Sliding Wardrobe with Loft'),
      (4, 'Openable Wardrobe with Loft'),
      (5, 'NA'),

   ]

   KBR_COT =  [
      (1, 'King Size'),
      (2, 'Queen Size'),
      (3, 'NA'),
   ]

   KBR_Reqs = [
      (1, 'Chest Of Drawer'),
      (2, 'Dresser'),
      (3, 'Bay Window'),
      (4, 'Dresser ,  Chest Of Drawer'),
      (5, 'Bay window ,Chest Of Drawer ,Dresser and Study'),
      (6, 'Bay window ,  Dresser ,  Study , Wallpaper'),
      (7, 'Bay window ,  Dresser ,  Study , Wallpaper, Painting'),
      (8, 'NA'),

   ]


   Four_BR_Wardrobe = [
      (1, 'Sliding Wardrobe'),
      (2, 'Openable Wardrobe'),
      (3, 'Sliding Wardrobe with Loft'),
      (4, 'Openable Wardrobe with Loft'),
      (5, 'NA'),


   ]


   Four_BR_COT =  [
      (1, 'King Size'),
      (2, 'Queen Size'),
      (3, 'NA'),
   ]

   Four_BR_Reqs = [
      (1, 'Chest Of Drawer'),
      (2, 'Dresser'),
      (3, 'Bay Window'),
      (4, 'Dresser ,  Chest Of Drawer'),
      (5, 'Bay window ,Chest Of Drawer ,Dresser and Study'),
      (6, 'Bay window ,  Dresser ,  Study , Wallpaper'),
      (7, 'Bay window ,  Dresser ,  Study , Wallpaper, Painting'),
      (8, 'NA'),
   ]


   Five_BR_Wardrobe = [
      (1, 'Sliding Wardrobe'),
      (2, 'Openable Wardrobe'),
      (3, 'Sliding Wardrobe with Loft'),
      (4, 'Openable Wardrobe with Loft'),
      (5, 'NA'),

   ]

   Five_BR_COT =  [
      (1, 'King Size'),
      (2, 'Queen Size'),
      (3, 'NA'),
   ]

   Five_BR_Reqs = [
      (1, 'Chest Of Drawer'),
      (2, 'Dresser'),
      (3, 'Bay Window'),
      (4, 'Dresser ,  Chest Of Drawer'),
      (5, 'Bay window ,Chest Of Drawer ,Dresser and Study'),
      (6, 'Bay window ,  Dresser ,  Study , Wallpaper'),
      (7, 'Bay window ,  Dresser ,  Study , Wallpaper, Painting'),
      (8, 'NA'),

   ]

   Livingroom = [
      (1, 'TV unit'),
      (2, 'TV unit, Partition'),
      (3, 'TV unit, Partition, False ceiling'),
      (4, 'TV unit, Partition, False ceiling, Wallpaper'),
      (5, 'TV unit, Partition, False ceiling, Wallpaper, Wall Panelling'),
      (6, 'TV unit, Partition, False ceiling, Wallpaper, Wall Panelling, Sofa'),
      (7, 'TV unit, Partition, False ceiling, Wallpaper, Wall Panelling, Sofa, Centre Table'),
      (8, 'TV unit, Partition, False ceiling, Wallpaper, Wall Panelling, Sofa, Centre Table, Curtains'),
      (9, 'NA'),
   ]

   Diningroom = [
      (1, 'Crockery Unit'),
      (2, 'Crockery Unit, False ceiling'),
      (3, 'Crockery Unit, False ceiling, Dining table & Chairs'),
      (4, 'Crockery Unit, False ceiling, Dining table & Chairs, Partition'),
      (5, 'Crockery Unit, False ceiling, Dining table & Chairs, Partition, Wallpaper'),
      (6, 'Crockery Unit, False ceiling, Dining table & Chairs, Partition, Wallpaper, Curtains'),
      (7, 'NA'),
   ]

   Washroom  = [
      (1, 'Vanity'),
      (2, 'Vanity, Shower Partition'),
      (3, 'Vanity, Shower Partition, Mirror '),
      (4, 'NA'),
   ]

   Foyer  = [
      (1, 'Shoe rack'),
      (2, 'Shoe rack, Foyer unit'),
      (3, 'Shoe rack, Foyer unit, Wallpaper'),
      (4, 'Shoe rack, Foyer unit, Wallpaper, Wall panelling'),
      (5, 'Shoe rack, Foyer unit, Wallpaper, Wall panelling, False ceiling'),
      (6, 'NA'),
   ]


   




   designer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='designer_checklist')
   customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_checklist')
   project_name = models.CharField(max_length=100, null=True)
   project_category = models.IntegerField(choices=category)

   project_type = models.IntegerField(choices=type)
   

   kitchen_finish = models.IntegerField(choices=k_finishes)
   kitchen_countertop = models.IntegerField(choices=k_countertop)
   kitchen_dado = models.IntegerField(choices=k_dado)
   kitchen_loft = models.IntegerField(choices=k_loft)
   utility = models.IntegerField(choices=utilities)

   MBR_Wardrobe = models.IntegerField(choices=MBR_Wardrobe)
   MBR_COT = models.IntegerField(choices=MBR_COT)
   MBR_Reqs = models.IntegerField(choices=MBR_Reqs)

   GBR_Wardrobe = models.IntegerField(choices=GBR_Wardrobe)
   GBR_COT = models.IntegerField(choices=GBR_COT)
   GBR_Reqs = models.IntegerField(choices=GBR_Reqs)

   KBR_Wardrobe = models.IntegerField(choices=KBR_Wardrobe)
   KBR_COT = models.IntegerField(choices=KBR_COT)
   KBR_Reqs = models.IntegerField(choices=KBR_Reqs)

   Four_BR_Wardrobe = models.IntegerField(choices=Four_BR_Wardrobe)
   Four_BR_COT = models.IntegerField(choices=Four_BR_COT)
   Four_BR_Reqs = models.IntegerField(choices=Four_BR_Reqs)   

   Five_BR_Wardrobe = models.IntegerField(choices=Five_BR_Wardrobe)
   Five_BR_COT = models.IntegerField(choices=Five_BR_COT)
   Five_BR_Reqs = models.IntegerField(choices=Five_BR_Reqs)

   Livingroom = models.IntegerField(choices=Livingroom)
   Diningroom = models.IntegerField(choices=Diningroom)
   Washroom = models.IntegerField(choices=Washroom)
   Foyer = models.IntegerField(choices=Foyer)

   Requirements = models.TextField(null=True)



   floor_plan = models.ImageField(upload_to='users/floorplan', blank=True, null=True)



   def __str__(self):
        return f"{self.designer.username} - {self.customer.username}"




    