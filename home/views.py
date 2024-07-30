"""
Views for handling the index page and carousel management.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from products.models import Product
import random
from .models import Carousel
from .forms import CarouselForm


class AdminOrSuperuserRequiredMixin(UserPassesTestMixin):
    """Mixin to allow only admin or superuser access."""

    def test_func(self):
        """
        Test if the user is staff or superuser.

        Returns:
            bool: True if the user is staff or superuser.
        """
        return self.request.user.is_staff or self.request.user.is_superuser


class IndexView(View):
    """A view to return the index page with products, deal products,
    and carousel items.
    """

    def get_pagination_range(self, page_obj):
        """
        Get the range of pages for pagination display.

        Args:
            page_obj (Page): The page object.

        Returns:
            list: The range of pages to display.
        """
        if not page_obj:
            return []

        num_pages = page_obj.paginator.num_pages
        current_page = page_obj.number

        # Set the range of pages to display
        start = max(current_page - 1, 1)
        end = min(current_page + 1, num_pages)

        page_range = range(start, end + 1)

        # Add ellipses if necessary
        if start > 2:
            page_range = [1, '...'] + list(page_range)
        if end < num_pages - 1:
            page_range = list(page_range) + ['...', num_pages]

        return page_range

    def get(self, request):
        """
        Handle GET requests to display the index page.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: The rendered index page.
        """
        context = {}

        # Pagination for deal products
        deals_list = list(Product.objects.filter(is_on_deal=True))
        random.shuffle(deals_list)
        deals_paginator = Paginator(deals_list, 6)
        deals_page = request.GET.get('deals_page')
        deals = deals_paginator.get_page(deals_page)
        context['deal_products'] = deals
        context['deal_page_obj'] = deals
        context['is_deal_paginated'] = deals.has_other_pages()
        context['deal_page_range'] = self.get_pagination_range(deals)

        # Pagination for all products
        products_list = list(Product.objects.all())
        random.shuffle(products_list)
        paginator = Paginator(products_list, 12)
        page = request.GET.get('page')
        products = paginator.get_page(page)
        context['all_products'] = products
        context['all_page_obj'] = products
        context['is_all_paginated'] = products.has_other_pages()
        context['all_page_range'] = self.get_pagination_range(products)

        # Add carousel items to the context
        carousel_items = Carousel.objects.all()
        context['carousel_items'] = carousel_items

        return render(request, 'home/index.html', context)


# Carousel Management Views

class CarouselListView(
    LoginRequiredMixin, AdminOrSuperuserRequiredMixin, View
):
    """View to list all carousel items."""

    def get(self, request):
        """
        Handle GET requests to display all carousel items.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: The rendered carousel management page.
        """
        carousels = Carousel.objects.all()
        return render(
            request,
            'carousel_management/carousel_management.html',
            {'carousels': carousels}
        )


class CarouselCreateView(
    LoginRequiredMixin, AdminOrSuperuserRequiredMixin, View
):
    """View to create a new carousel item."""

    def get(self, request):
        """
        Handle GET requests to display the carousel creation form.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: The rendered add carousel page.
        """
        form = CarouselForm()
        return render(
            request,
            'carousel_management/add_carousel.html',
            {'form': form}
        )

    def post(self, request):
        """
        Handle POST requests to create a new carousel item.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: Redirects to the carousel list page if form is valid,
            otherwise renders the add carousel page with errors.
        """
        form = CarouselForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('carousel_list')
        return render(
            request,
            'carousel_management/add_carousel.html',
            {'form': form}
        )


class CarouselUpdateView(
    LoginRequiredMixin, AdminOrSuperuserRequiredMixin, View
):
    """View to update an existing carousel item."""

    def get(self, request, pk):
        """
        Handle GET requests to display the carousel update form.

        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): Primary key of the carousel item.

        Returns:
            HttpResponse: The rendered edit carousel page.
        """
        carousel = get_object_or_404(Carousel, pk=pk)
        form = CarouselForm(instance=carousel)
        return render(
            request,
            'carousel_management/edit_carousel.html',
            {'form': form}
        )

    def post(self, request, pk):
        """
        Handle POST requests to update an existing carousel item.

        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): Primary key of the carousel item.

        Returns:
            HttpResponse: Redirects to the carousel list page if form is valid,
            otherwise renders the edit carousel page with errors.
        """
        carousel = get_object_or_404(Carousel, pk=pk)
        form = CarouselForm(
            request.POST, request.FILES, instance=carousel
        )
        if form.is_valid():
            form.save()
            return redirect('carousel_list')
        return render(
            request,
            'carousel_management/edit_carousel.html',
            {'form': form}
        )


class CarouselDeleteView(
    LoginRequiredMixin, AdminOrSuperuserRequiredMixin, View
):
    """View to delete an existing carousel item."""

    def post(self, request, pk):
        """
        Handle POST requests to delete a carousel item.

        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): Primary key of the carousel item.

        Returns:
            HttpResponse: Redirects to the carousel list page.
        """
        carousel = get_object_or_404(Carousel, pk=pk)
        if carousel.image:
            carousel.image.delete(save=False)
        carousel.delete()
        return redirect('carousel_list')