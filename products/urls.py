from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ProductListView, ProductDetailView, AddProductView, EditProductView, ProductDeleteView, ProductManagementView

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
    path('add/', AddProductView.as_view(), name='add_product'),
    path('edit/<int:pk>/', EditProductView.as_view(), name='edit_product'),
    path('delete/<int:product_id>/', ProductDeleteView.as_view(), name='delete_product'),
    path('product_management/', ProductManagementView.as_view(), name='product_management'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)