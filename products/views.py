from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import redirect, reverse
from django.utils import timezone
from .models import Product, Collection, Creator, Category
import datetime

class FilteredProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        sort = self.request.GET.get('sort')
        collection = self.request.GET.get('collection')
        category = self.request.GET.get('category')
        creator = self.request.GET.get('creator')
        is_on_deal = self.request.GET.get('is_on_deal')
        new_arrivals = self.request.GET.get('new_arrivals')

        if query:
            queries = (Q(name__icontains=query) | 
                       Q(description__icontains=query) | 
                       Q(collection__friendly_name__icontains=query) | 
                       Q(creator__name__icontains=query))
            queryset = queryset.filter(queries)

        if collection:
            queryset = queryset.filter(collection__id=collection)
        
        if category:
            queryset = queryset.filter(category__id=category)

        if creator:
            queryset = queryset.filter(creator__id=creator)

        if is_on_deal:
            queryset = queryset.filter(is_on_deal=True)

        if new_arrivals:
            thirty_days_ago = timezone.now() - datetime.timedelta(days=30)
            queryset = queryset.filter(created_at__gte=thirty_days_ago)

        if sort:
            if sort == 'name_asc':
                queryset = queryset.order_by('name')
            elif sort == 'name_desc':
                queryset = queryset.order_by('-name')
            elif sort == 'price_asc':
                queryset = queryset.order_by('price')
            elif sort == 'price_desc':
                queryset = queryset.order_by('-price')
            elif sort == 'rating_desc':
                queryset = queryset.order_by('-rating')
            elif sort == 'category':
                queryset = queryset.order_by('category__friendly_name')
        else:
            # Default ordering
            queryset = queryset.order_by('name')

        return queryset

class ProductListView(FilteredProductListView):
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort', 'name_asc')
        collection_id = self.request.GET.get('collection')
        category_id = self.request.GET.get('category')
        creator_id = self.request.GET.get('creator')
        is_on_deal = self.request.GET.get('is_on_deal')
        new_arrivals = self.request.GET.get('new_arrivals')
        
        context['search_term'] = query or ''
        context['current_sorting'] = sort
        
        current_filter = {
            'collection': None,
            'category': None,
            'creator': None,
            'is_on_deal': is_on_deal,
            'new_arrivals': new_arrivals,
        }
        
        if collection_id:
            current_filter['collection'] = Collection.objects.get(id=collection_id)
        if category_id:
            current_filter['category'] = Category.objects.get(id=category_id)
        if creator_id:
            current_filter['creator'] = Creator.objects.get(id=creator_id)
        
        context['current_filter'] = current_filter
        
        return context

    def get(self, request, *args, **kwargs):
        if 'q' in request.GET and not request.GET['q']:
            messages.error(request, "Please enter search criteria!")
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
