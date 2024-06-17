from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import redirect, reverse
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            queryset = queryset.filter(queries)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        if query:
            context['search_term'] = query
        return context

    def get(self, request, *args, **kwargs):
        if 'q' in request.GET and not request.GET['q']:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect(reverse('products'))
        return super().get(request, *args, **kwargs)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        product = context.get('product')
        if product and product.category:
            context['friendly_name'] = product.category.get_friendly_name()
        else:
            context['friendly_name'] = None
        context['range'] = range(1, 6)  # Range for 5 stars
        context['size_choices'] = Product.SIZE_CHOICES

        # Pagination logic
        products_list = Product.objects.all()
        paginator = Paginator(products_list, 3)  # Paginate by 3 items
        page = self.request.GET.get('page')
        products = paginator.get_page(page)
        context['products'] = products
        context['page_obj'] = products
        context['is_paginated'] = products.has_other_pages()

        return context