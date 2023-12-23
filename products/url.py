from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products.as_view(), name='products'),
]