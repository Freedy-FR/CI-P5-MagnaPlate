from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.views import View


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
        cart = request.session.get('cart', {})

        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect(redirect_url)