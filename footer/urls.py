from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('subscribe/', NewsletterSubscriptionView.as_view(), name='subscribe_newsletter'),
    path('create-newsletter/', CreateNewsletterEmailView.as_view(), name='create_newsletter'),
    path('send-newsletters/', SendNewslettersView.as_view(), name='send_newsletters'),
    path('edit-newsletter/<int:pk>/', EditNewsletterView.as_view(), name='edit_newsletter'),
    path('about-us/', AboutUsView.as_view(), name='about_us'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
