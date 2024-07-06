from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.views import View

from .forms import OrderForm


class CheckoutView(View):
    def get(self, request, *args, **kwargs):
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "There's nothing in your cart at the moment")
            return redirect(reverse('products'))

        order_form = OrderForm()
        template = 'checkout.html'
        context = {
            'order_form': order_form,
        }

        return render(request, template, context)
