from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
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

        # Render the template with context
        return render(request, 'home/index.html', context)