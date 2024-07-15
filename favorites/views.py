from django.views.generic import ListView, View
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import FavoriteProduct, FavoriteCreator
from products.models import Product, Creator

class FavoriteListView(LoginRequiredMixin, ListView):
    template_name = 'favorite.html'
    
    def get_queryset(self):
        return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['favorite_products'] = FavoriteProduct.objects.filter(user=user)
        context['favorite_creators'] = FavoriteCreator.objects.filter(user=user)
        context['username'] = user.username
        return context

class ToggleFavoriteProductView(LoginRequiredMixin, View):
    def post(self, request, id):
        product = get_object_or_404(Product, id=id)
        favorite, created = FavoriteProduct.objects.get_or_create(user=request.user, product=product)
        if created:
            favorite.is_favorite = True
            favorite.save()
            messages.success(request, f'{product.name} has been added to your favorites.')
        else:
            favorite.is_favorite = not favorite.is_favorite
            if not favorite.is_favorite:
                favorite.delete()
                messages.info(request, f'{product.name} has been removed from your favorites.')
            else:
                favorite.save()
                messages.success(request, f'{product.name} has been added to your favorites.')
        return redirect(request.META.get('HTTP_REFERER', '/'))

class ToggleFavoriteCreatorView(LoginRequiredMixin, View):
    def post(self, request, id):
        creator = get_object_or_404(Creator, id=id)
        favorite, created = FavoriteCreator.objects.get_or_create(user=request.user, creator=creator)
        if created:
            favorite.is_favorite = True
            favorite.save()
            messages.success(request, f'{creator.name} has been added to your favorites.')
        else:
            favorite.is_favorite = not favorite.is_favorite
            if not favorite.is_favorite:
                favorite.delete()
                messages.info(request, f'{creator.name} has been removed from your favorites.')
            else:
                favorite.save()
                messages.success(request, f'{creator.name} has been added to your favorites.')
        return redirect(request.META.get('HTTP_REFERER', '/'))
