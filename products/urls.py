from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from products.views import *


urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),

    # Product Management
    path('add/', AddProductView.as_view(), name='add_product'),
    path('edit/<int:pk>/', EditProductView.as_view(), name='edit_product'),
    path('delete/<int:product_id>/', ProductDeleteView.as_view(), name='delete_product'),
    path('product_management/', ProductManagementView.as_view(), name='product_management'),

    # Category Management
    path('category_management/', CategoryManagementView.as_view(), name='category_management'),
    path('categories/add/', CategoryCreateView.as_view(), name='add_category'),
    path('categories/edit/<int:pk>/', CategoryUpdateView.as_view(), name='edit_category'),
    path('categories/delete/<int:pk>/', CategoryDeleteView.as_view(), name='delete_category'),

    # Collections Management
    path('collections/add/', CollectionCreateView.as_view(), name='add_collection'),
    path('collections/edit/<int:pk>/', CollectionUpdateView.as_view(), name='edit_collection'),
    path('collections/delete/<int:pk>/', CollectionDeleteView.as_view(), name='delete_collection'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)