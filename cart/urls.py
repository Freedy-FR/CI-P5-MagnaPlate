"""
URL configuration for the cart application.

This module defines the URL patterns for the cart application,
including views for viewing, adding to, updating, and removing from the cart.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (
    ViewCart, AddToCartView, UpdateCartView, RemoveFromCartView
)

urlpatterns = [
    path('', ViewCart.as_view(), name='view_cart'),
    path(
        'add_to_cart/<int:item_id>/',
        AddToCartView.as_view(),
        name='add_to_cart'
    ),
    path(
        'update/<int:item_id>/',
        UpdateCartView.as_view(),
        name='update_cart'
    ),
    path(
        'remove/<int:item_id>/',
        RemoveFromCartView.as_view(),
        name='remove_from_cart'
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
