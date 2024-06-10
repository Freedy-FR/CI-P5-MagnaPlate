from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.views import View
from cart.contexts import cart_contents  # Import the cart_contents function
from products.models import Product #Testing the information being sent to cart


class ViewCart(TemplateView):
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Debugging: Print the context
        print("Context passed to template:", context)

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

        # Debugging: Print the current cart contents before modification
        print("Current Cart Contents Before Modification:", cart)

        if size:
            if str(item_id) in cart:
                # Check if 'items_by_size' already exists for the item
                if 'items_by_size' in cart[str(item_id)]:
                    if size in cart[str(item_id)]['items_by_size']:
                        cart[str(item_id)]['items_by_size'][size] += quantity
                    else:
                        cart[str(item_id)]['items_by_size'][size] = quantity
                else:
                    cart[str(item_id)]['items_by_size'] = {size: quantity}
            else:
                cart[str(item_id)] = {'items_by_size': {size: quantity}}
        else:
            if str(item_id) in cart:
                if isinstance(cart[str(item_id)], dict):
                    cart[str(item_id)]['quantity'] += quantity
                else:
                    cart[str(item_id)] += quantity
            else:
                cart[str(item_id)] = quantity

        request.session['cart'] = cart

        # Debugging: Print the updated cart contents after modification
        print("Updated Cart Contents After Modification:", cart)

        # Printing content in cart for debugging
        print("POST Data:", request.POST)
        print("Cart Contents:")
        for key, value in cart.items():
            product = get_object_or_404(Product, pk=key)
            print(f"Item ID: {key}, Product: {product.name}")
            if isinstance(value, int):
                print(f"Quantity: {value}")
            else:
                print(f"Items by Size: {value['items_by_size']}")

        return redirect(redirect_url)
