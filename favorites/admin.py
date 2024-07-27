"""
Admin configuration for the favorites application.

This module registers the FavoriteProduct and FavoriteCreator models
with the Django admin site and optionally customizes their admin interfaces.
"""

from django.contrib import admin
from .models import FavoriteProduct, FavoriteCreator


class FavoriteProductAdmin(admin.ModelAdmin):
    """
    Admin configuration for the FavoriteProduct model.
    """
    list_display = ('user', 'product', 'created_at')
    search_fields = ('user__username', 'product__name')
    list_filter = ('created_at',)


class FavoriteCreatorAdmin(admin.ModelAdmin):
    """
    Admin configuration for the FavoriteCreator model.
    """
    list_display = ('user', 'creator', 'created_at')
    search_fields = ('user__username', 'creator__name')
    list_filter = ('created_at',)


# Register the models with the admin site
admin.site.register(FavoriteProduct, FavoriteProductAdmin)
admin.site.register(FavoriteCreator, FavoriteCreatorAdmin)
