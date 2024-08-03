"""
Admin configuration for Carousel model.
"""

from django.contrib import admin
from .models import Carousel


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    """Admin view for managing Carousel objects."""

    list_display = ['id', 'caption', 'order', 'link']
    list_editable = ['order']
