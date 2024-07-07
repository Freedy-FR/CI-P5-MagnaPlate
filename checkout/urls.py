from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from .views import CheckoutView, CheckoutSuccessView
from products.views import ProductListView
from .webhooks import webhook


urlpatterns = [
    path('', CheckoutView.as_view(), name='checkout'),
    path('products/', ProductListView.as_view(), name='products'),
    path('success/<order_number>/', CheckoutSuccessView.as_view(), name='checkout_success'),
    path('wh/', webhook, name='webhook'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)