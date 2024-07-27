"""
URL configuration for the app.
"""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import (
    IndexView, CarouselListView, CarouselCreateView,
    CarouselUpdateView, CarouselDeleteView
)

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path(
        'carousel_management/',
        CarouselListView.as_view(),
        name='carousel_list'
    ),
    path(
        'carousel_management/add/',
        CarouselCreateView.as_view(),
        name='carousel_create'
    ),
    path(
        'carousel_management/<int:pk>/edit/',
        CarouselUpdateView.as_view(),
        name='carousel_update'
    ),
    path(
        'carousel_management/<int:pk>/delete/',
        CarouselDeleteView.as_view(),
        name='carousel_delete'
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
