from django import forms
from .models import Builder , Builder_OpeningHour


class BuilderForm(forms.ModelForm):
    class Meta:
        model = Builder
        fields = ['builder_name', 'builder_license' , 'builder_description' , 'offical_number' , 'website' , 'experience' , 'facebook_link' , 'youtube_link' , 'instagram_link']




class Builder_OpeningHourForm(forms.ModelForm):
    class Meta:
        model = Builder_OpeningHour
        fields = ['day', 'from_hour', 'to_hour', 'is_closed']