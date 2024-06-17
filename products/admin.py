from django.contrib import admin
from .models import Category, Product, Collection, Creator

class CollectionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
        'collection',
    )

class CreatorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'category',
        'collection',
        'creator',
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
        'creator__name',
    )

admin.site.register(Collection, CollectionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Creator, CreatorAdmin)
admin.site.register(Product, ProductAdmin)
