"""
URL configuration for the checkout application.

This module defines the URL patterns for the checkout process, including
views for the checkout page, checkout success page, cache checkout data,
and webhooks.
"""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import CheckoutView, CheckoutSuccessView, CacheCheckoutDataView
from .webhooks import webhook

urlpatterns = [
    path('', CheckoutView.as_view(), name='checkout'),
    path(
        'success/<order_number>/',
        CheckoutSuccessView.as_view(),
        name='checkout_success'
    ),
    path(
        'cache_checkout_data/',
        CacheCheckoutDataView.as_view(),
        name='cache_checkout_data'
    ),
    path('wh/', webhook, name='webhook'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
