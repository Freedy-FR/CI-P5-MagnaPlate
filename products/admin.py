"""
Admin configuration for managing models in the admin interface.
"""

from django.contrib import admin
from .models import Category, Product, Collection, Creator


class CollectionAdmin(admin.ModelAdmin):
    """Admin view for managing Collection instances."""

    list_display = (
        'name',
        'friendly_name',
    )


class CategoryAdmin(admin.ModelAdmin):
    """Admin view for managing Category instances."""

    list_display = (
        'name',
        'friendly_name',
        'collection',
    )


class CreatorAdmin(admin.ModelAdmin):
    """Admin view for managing Creator instances."""

    list_display = (
        'name',
        'description',
        'image',
    )
    search_fields = (
        'name',
        'description',
    )


class ProductAdmin(admin.ModelAdmin):
    """Admin view for managing Product instances."""

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
