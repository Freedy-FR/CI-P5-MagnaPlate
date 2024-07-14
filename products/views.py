from django.views.generic.list import ListView
from django.views.generic import DetailView, TemplateView
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.utils import timezone
from .models import Product, Collection, Creator, Category, Creator
from .forms import *
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
        context['page_range'] = self.get_pagination_range(products)

        return context

    def get_pagination_range(self, page_obj):
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


# Creators Views

class AllCreatorsView(ListView):
    model = Creator
    template_name = 'creators/all_creators.html'
    context_object_name = 'creators'
    paginate_by = 6  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_range'] = self.get_pagination_range(context['page_obj'])
        return context

    def get_pagination_range(self, page_obj):
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

class CreatorDetailView(DetailView):
    model = Creator
    template_name = 'creators/creator_detail.html'
    context_object_name = 'creator'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        creator = self.get_object()

        collections = creator.products.values_list('collection__friendly_name', flat=True).distinct()
        categories = creator.products.values_list('category__friendly_name', flat=True).distinct()

        context['collections'] = collections
        context['categories'] = categories

        products_list = creator.products.all()
        paginator = Paginator(products_list, 6)
        page = self.request.GET.get('page')
        products = paginator.get_page(page)
        context['products'] = products
        context['page_obj'] = products
        context['is_paginated'] = products.has_other_pages()
        context['page_range'] = self.get_pagination_range(products)
        
        return context

    def get_pagination_range(self, page_obj):
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

# Product Management Views

class ProductManagementView(LoginRequiredMixin, ListView):
    template_name = 'product_management/product_management.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 12

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
            return redirect(reverse('product_management'))
        return super().get(request, *args, **kwargs)


class AddProductView(LoginRequiredMixin, View):
    """ Add a product to the store """

    def get(self, request, *args, **kwargs):
        form = ProductForm()
        template = 'product_management/add_product.html'
        context = {
            'form': form,
        }
        return render(request, template, context)

    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')

        template = 'add_product.html'
        context = {
            'form': form,
        }
        return render(request, template, context)


class EditProductView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_management/edit_product.html'
    
    def form_valid(self, form):
        messages.success(self.request, 'Successfully updated product!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Failed to update product. Please ensure the form is valid.')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('product_detail', args=[self.object.id])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = self.object
        messages.info(self.request, f'You are editing {self.object.name}')
        return context


class ProductDeleteView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        product_id = kwargs.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect(reverse_lazy('product_management'))


# Creators Management Views

class CreatorManagementView(LoginRequiredMixin, ListView):
    model = Creator
    template_name = 'creator_management/creator_management.html'
    context_object_name = 'creators'
    paginate_by = 12

class CreatorCreateView(LoginRequiredMixin, CreateView):
    model = Creator
    form_class = CreatorForm
    template_name = 'creator_management/add_creator.html'
    success_url = reverse_lazy('creator_management')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Successfully added creator: {self.object.name}!')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Failed to add creator. Please ensure the form is valid.')
        return super().form_invalid(form)

class CreatorUpdateView(LoginRequiredMixin, UpdateView):
    model = Creator
    form_class = CreatorForm
    template_name = 'creator_management/edit_creator.html'
    success_url = reverse_lazy('creator_management')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Successfully updated creator: {self.object.name}!')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Failed to update creator. Please ensure the form is valid.')
        return super().form_invalid(form)

class CreatorDeleteView(LoginRequiredMixin, DeleteView):
    model = Creator
    template_name = 'creator_management/delete_creator.html'
    success_url = reverse_lazy('creator_management')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(self.request, f'Creator {self.object.name} deleted successfully!')
        return super().delete(request, *args, **kwargs)


# Category Management Views

class CategoryManagementView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'category_management/category_management.html'
    context_object_name = 'categories'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CategoryForm()
        return context


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_management/add_category.html'
    success_url = reverse_lazy('category_management')

    def form_valid(self, form):
        messages.success(self.request, 'Successfully added category!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Failed to add category. Please ensure the form is valid.')
        return super().form_invalid(form)

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_management/edit_category.html'
    success_url = reverse_lazy('category_management')

    def form_valid(self, form):
        messages.success(self.request, 'Successfully updated category!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Failed to update category. Please ensure the form is valid.')
        return super().form_invalid(form)

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'category_management/delete_category.html'
    success_url = reverse_lazy('category_management')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Category deleted successfully!')
        return super().delete(request, *args, **kwargs)


# Collection Management Views

class CollectionManagementView(LoginRequiredMixin, ListView):
    model = Collection
    template_name = 'collection_management/collection_management.html'
    context_object_name = 'collections'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CollectionForm()
        return context

class CollectionCreateView(LoginRequiredMixin, CreateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collection_management/add_collection.html'
    success_url = reverse_lazy('collection_management')

    def form_valid(self, form):
        messages.success(self.request, 'Successfully added collection!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Failed to add collection. Please ensure the form is valid.')
        return super().form_invalid(form)

class CollectionUpdateView(LoginRequiredMixin, UpdateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collection_management/edit_collection.html'
    success_url = reverse_lazy('collection_management')

    def form_valid(self, form):
        messages.success(self.request, 'Successfully updated collection!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Failed to update collection. Please ensure the form is valid.')
        return super().form_invalid(form)

class CollectionDeleteView(LoginRequiredMixin, DeleteView):
    model = Collection
    template_name = 'collection_management/delete_collection.html'
    success_url = reverse_lazy('collection_management')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Collection deleted successfully!')
        return super().delete(request, *args, **kwargs)