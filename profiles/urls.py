"""
URL configuration for the profiles app.
"""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    ProfileView, OrderHistoryView, SiteManagementView
)

urlpatterns = [
    path(
        '', ProfileView.as_view(), name='profile'
    ),
    path(
        'order_history/<str:order_number>/',
        OrderHistoryView.as_view(),
        name='order_history'
    ),
    path(
        'site_management/',
        SiteManagementView.as_view(),
        name='site_management'
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
