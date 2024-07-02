from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from products.models import Product

class IndexView(View):
    """ A view to return the index page with products and deal products. """

    def get(self, request):
        # Get all products
        products = Product.objects.all()

        # Get products on deal
        deal_products = Product.objects.filter(is_on_deal=True)

        # Prepare the context
        context = {
            'products': products,
            'deal_products': deal_products
        }

        deals_list = Product.objects.filter(is_on_deal=True)
        deals_paginator = Paginator(deals_list, 6)  # Paginate by 3 items for deals
        deals_page = self.request.GET.get('deals_page')
        deals = deals_paginator.get_page(deals_page)
        context['deal_products'] = deals
        context['deal_page_obj'] = deals
        context['is_deal_paginated'] = deals.has_other_pages()

        # Render the template with context
        return render(request, 'home/index.html', context)