from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from products.models import Product

class IndexView(View):
    """ A view to return the index page """

    def get(self, request):
        return render(request, 'home/index.html')

    def get(self, request):
        context = {'products': Product.objects.all()}
        return render(request, 'home/index.html', context)