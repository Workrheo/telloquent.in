from django import forms
from .models import Designer , OpeningHour


class DesignerForm(forms.ModelForm):
    class Meta:
        model = Designer
        fields = ['designer_name', 'designer_license' , 'designer_description' , 'offical_number' , 'website' , 'experience' , 'facebook_link' , 'youtube_link' , 'instagram_link']




class OpeningHourForm(forms.ModelForm):
    class Meta:
        model = OpeningHour
        fields = ['day', 'from_hour', 'to_hour', 'is_closed']