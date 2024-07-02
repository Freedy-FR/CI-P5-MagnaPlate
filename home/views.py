from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from products.models import Product

class IndexView(View):
    """ A view to return the index page with products and deal products. """

    def get(self, request):
        # Prepare the context
        context = {}

        # Pagination for deal products
        deals_list = Product.objects.filter(is_on_deal=True)
        deals_paginator = Paginator(deals_list, 6)  # Paginate by 6 items for deals
        deals_page = request.GET.get('deals_page')
        deals = deals_paginator.get_page(deals_page)
        context['deal_products'] = deals
        context['deal_page_obj'] = deals
        context['is_deal_paginated'] = deals.has_other_pages()

        # Pagination for all products
        products_list = Product.objects.all()
        paginator = Paginator(products_list, 12)  # Paginate by 12 items for all products
        page = request.GET.get('page')
        products = paginator.get_page(page)
        context['all_products'] = products
        context['all_page_obj'] = products
        context['is_all_paginated'] = products.has_other_pages()

        # Render the template with context
        return render(request, 'home/index.html', context)
