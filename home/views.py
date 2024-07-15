from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from products.models import Product
import random
from .models import Carousel

class IndexView(View):
    """ A view to return the index page with products, deal products, and carousel items. """

    def get_pagination_range(self, page_obj):
        if not page_obj:
            return []

        num_pages = page_obj.paginator.num_pages
        current_page = page_obj.number

        # Set the range of pages to display
        start = max(current_page - 1, 1)  # Show 1 page before the current page
        end = min(current_page + 1, num_pages)  # Show 1 page after the current page
        
        page_range = range(start, end + 1)

        # Add ellipses if necessary
        if start > 2:
            page_range = [1, '...'] + list(page_range)
        if end < num_pages - 1:
            page_range = list(page_range) + ['...', num_pages]

        return page_range

    def get(self, request):
        # Prepare the context
        context = {}

        # Pagination for deal products
        deals_list = list(Product.objects.filter(is_on_deal=True))  # Convert to list
        random.shuffle(deals_list)  # Shuffle the list
        deals_paginator = Paginator(deals_list, 6)  # Paginate by 6 items for deals
        deals_page = request.GET.get('deals_page')
        deals = deals_paginator.get_page(deals_page)
        context['deal_products'] = deals
        context['deal_page_obj'] = deals
        context['is_deal_paginated'] = deals.has_other_pages()
        context['deal_page_range'] = self.get_pagination_range(deals)

        # Pagination for all products
        products_list = list(Product.objects.all())  # Convert to list
        random.shuffle(products_list)  # Shuffle the list
        paginator = Paginator(products_list, 12)  # Paginate by 12 items for all products
        page = request.GET.get('page')
        products = paginator.get_page(page)
        context['all_products'] = products
        context['all_page_obj'] = products
        context['is_all_paginated'] = products.has_other_pages()
        context['all_page_range'] = self.get_pagination_range(products)

        # Add carousel items to the context
        carousel_items = Carousel.objects.all()
        context['carousel_items'] = carousel_items

        # Render the template with context
        return render(request, 'home/index.html', context)
