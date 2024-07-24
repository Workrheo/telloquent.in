from django.contrib import admin
from .models import Category , PortfolioItem , Architect_Category , Architect_PortfolioItem


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'designer', 'updated_at')
    search_fields = ('category_name', 'designer__designer_name')

class Architect_CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'architect', 'updated_at')
    search_fields = ('category_name', 'architect__architect_name')



#class PortfolioItemAdmin(admin.ModelAdmin):
    #prepopulated_fields = {'slug': ('project_title',)}
    #list_display = ('project_title', 'category', 'designer', 'price', 'is_available', 'updated_at')
    #search_fields = ('project_title', 'category__category_name', 'designer__designer_name', 'price')
    #list_filter = ('is_available',)

# Register your models here.

admin.site.register(Category, CategoryAdmin)
admin.site.register(PortfolioItem ) #PortfolioItemAdmin)
admin.site.register(Architect_Category, Architect_CategoryAdmin)
admin.site.register(Architect_PortfolioItem ) #PortfolioItemAdmin)
