from tabnanny import verbose
from django.db import models
from designer.models import Designer
from architects.models import Architect
from builder.models import Builder

# Create your models here.
class Category(models.Model):
    designer = models.ForeignKey(Designer, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=50)
    property_name = models.CharField(max_length=50 , null=True)
    project_image = models.ImageField(null=True, blank=True , upload_to='foodimages')
    project_created_at = models.DateField(null=True, blank=True)


    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=250, blank=True)
    project_budget = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def clean(self):
        self.category_name = self.category_name.capitalize()
    
    def __str__(self):
        return self.category_name



class PortfolioItem(models.Model):
    designer = models.ForeignKey(Designer, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='portfolioitems')
    image = models.ImageField(upload_to='foodimages')
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category.category_name



class Architect_Category(models.Model):
    architect = models.ForeignKey(Architect, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=50)
    property_name = models.CharField(max_length=50 , null=True , blank=True)
    project_image = models.ImageField(null=True, blank=True , upload_to='foodimages')
    project_created_at = models.DateField(null=True, blank=True)


    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=250, blank=True)
    project_budget = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Architect_category'
        verbose_name_plural = 'Architect_categories'

    def clean(self):
        self.category_name = self.category_name.capitalize()
    
    def __str__(self):
        return self.category_name



class Architect_PortfolioItem(models.Model):
    architect = models.ForeignKey(Architect, on_delete=models.CASCADE)
    category = models.ForeignKey(Architect_Category, on_delete=models.CASCADE, related_name='architect_portfolioitems')
    image = models.ImageField(upload_to='foodimages')
    price = models.PositiveBigIntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category.category_name
    




class Builder_Category(models.Model):
    builder = models.ForeignKey(Builder, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=50)
    property_name = models.CharField(max_length=50 , null=True , blank=True)
    project_image = models.ImageField(null=True, blank=True , upload_to='foodimages')
    project_created_at = models.DateField(null=True, blank=True)


    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=250, blank=True)
    project_budget = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Builder_Category'
        verbose_name_plural = 'Builder_categories'

    def clean(self):
        self.category_name = self.category_name.capitalize()
    
    def __str__(self):
        return self.category_name



class Builder_PortfolioItem(models.Model):
    builder = models.ForeignKey(Builder, on_delete=models.CASCADE)
    category = models.ForeignKey(Builder_Category, on_delete=models.CASCADE, related_name='architect_portfolioitems')
    image = models.ImageField(upload_to='foodimages')
    price = models.PositiveBigIntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category.category_name
