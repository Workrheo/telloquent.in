from django import forms
from .models import Appointment , Checklist , Architect_Appointment , Builder_Appointment



class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['a_date', 'a_timing', 'status', 'c_status']



class Architect_AppointmentForm(forms.ModelForm):
    class Meta:
        model = Architect_Appointment
        fields = ['a_date', 'a_timing', 'status', 'c_status']




class Builder_AppointmentForm(forms.ModelForm):
    class Meta:
        model = Builder_Appointment
        fields = ['a_date', 'a_timing', 'status', 'c_status']




class ChecklistForm(forms.ModelForm):
    class Meta:
        model = Checklist
        fields = [ 'project_name' , 'project_category', 'project_type', 'kitchen_finish', 'kitchen_countertop',
                  'kitchen_dado','kitchen_loft','utility','MBR_Wardrobe','MBR_COT','MBR_Reqs','GBR_Wardrobe','GBR_COT',
                  'GBR_Reqs','KBR_Wardrobe','KBR_COT','KBR_Reqs','Four_BR_Wardrobe','Four_BR_COT','Four_BR_Reqs','Five_BR_Wardrobe',
                  'Five_BR_COT','Five_BR_Reqs','Livingroom','Diningroom','Washroom','Foyer','Requirements','floor_plan' ,
                ]