from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from .views import ProfileView



urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)