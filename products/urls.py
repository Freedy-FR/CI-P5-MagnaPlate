from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from .views import AddProductView

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
    path('add/', AddProductView.as_view(), name='add_product'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)