from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import FavoriteListView, ToggleFavoriteProductView, ToggleFavoriteCreatorView

app_name = 'favorites'

urlpatterns = [
    path('', FavoriteListView.as_view(), name='favorite_list'),
    path('toggle_product/<int:id>/', ToggleFavoriteProductView.as_view(), name='toggle_favorite_product'),
    path('toggle_creator/<int:id>/', ToggleFavoriteCreatorView.as_view(), name='toggle_favorite_creator'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
