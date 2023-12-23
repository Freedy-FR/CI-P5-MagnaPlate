from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
        )

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'rating',
        'is_on_deal',
        )
    ordering = (
        'name',
        )
    search_fields = (
        'name',
        'description',
        )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
