from django.contrib import admin
from .models import FavoriteProduct, FavoriteCreator

admin.site.register(FavoriteProduct)
admin.site.register(FavoriteCreator)