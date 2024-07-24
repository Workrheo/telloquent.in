from django import forms
from accounts.validators import allow_only_images_validator
from .models import Category , PortfolioItem , Architect_Category , Architect_PortfolioItem , Builder_Category , Builder_PortfolioItem


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'description' , 'project_budget' , 'property_name' , 'project_image' , 'project_created_at']


class PortfolioItemForm(forms.ModelForm):
    image = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info w-100'}), validators=[allow_only_images_validator])
    class Meta:
        model = PortfolioItem
        fields = ['category', 'image', 'is_available']



class Architect_CategoryForm(forms.ModelForm):
    class Meta:
        model = Architect_Category
        fields = ['category_name', 'description' , 'project_budget' , 'property_name' , 'project_image' , 'project_created_at']


class Architect_PortfolioItemForm(forms.ModelForm):
    image = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info w-100'}), validators=[allow_only_images_validator])
    class Meta:
        model = Architect_PortfolioItem
        fields = ['category', 'image', 'description','price', 'is_available']



class Builder_CategoryForm(forms.ModelForm):
    class Meta:
        model = Builder_Category
        fields = ['category_name', 'description' , 'project_budget' , 'property_name' , 'project_image' , 'project_created_at']


class Builder_PortfolioItemForm(forms.ModelForm):
    image = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info w-100'}), validators=[allow_only_images_validator])
    class Meta:
        model = Builder_PortfolioItem
        fields = ['category', 'image', 'description','price', 'is_available']