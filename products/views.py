from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.core.paginator import Paginator
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 6



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