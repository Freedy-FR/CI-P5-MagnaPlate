from django.contrib import admin
from .models import Carousel

@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ['id', 'caption', 'order', 'link']
    list_editable = ['order']