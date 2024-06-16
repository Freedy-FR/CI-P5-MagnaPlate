from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', ViewCart.as_view(), name='view_cart'),
    path('add_to_cart/<int:item_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('update/<int:item_id>/', UpdateCartView.as_view(), name='update_cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)