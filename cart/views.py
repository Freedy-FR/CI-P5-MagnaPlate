from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.views import View
from products.models import Product #Testing the information being sent to cart


class ViewCart(TemplateView):
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class AddToCartView(View):
    """Add a quantity of the specified product to the shopping cart"""

    def post(self, request, item_id):
        quantity = int(request.POST.get('quantity'))
        redirect_url = request.POST.get('redirect_url')

        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']

        cart = request.session.get('cart', {})

        if size:
                if item_id in list(cart.keys()):
                    if size in cart[item_id]['items_by_size'].keys():
                        cart[item_id]['items_by_size'][size] += quantity
                    else:
                        cart[item_id]['items_by_size'][size] = quantity
                else:
                    cart[item_id] = {'items_by_size': {size: quantity}}
        else:
                if item_id in list(cart.keys()):
                    cart[item_id] += quantity
                else:
                    cart[item_id] = quantity

        request.session['cart'] = cart


        # Printing content in cart

        for key, value in cart.items():
            product = get_object_or_404(Product, pk=key)
            print(f"Key: {key}")
            print(f"Name: {product.name}")
            print(f"Quantity: {value}")
            print(f"Price: {product.price}")

        
        return redirect(redirect_url)