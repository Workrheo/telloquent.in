from django import forms
from .models import Architect , Architect_OpeningHour


class ArchitectForm(forms.ModelForm):
    class Meta:
        model = Architect
        fields = ['architect_name', 'architect_license' , 'architect_description' , 'offical_number' , 'website' , 'experience' , 'facebook_link' , 'youtube_link' , 'instagram_link']




class Architect_OpeningHourForm(forms.ModelForm):
    class Meta:
        model = Architect_OpeningHour
        fields = ['day', 'from_hour', 'to_hour', 'is_closed']