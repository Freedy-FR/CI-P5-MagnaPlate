from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.views import View
from django.contrib import messages
from cart.contexts import cart_contents  # Import the cart_contents function
from products.models import Product


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
        product = get_object_or_404(Product, pk=item_id)

        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']

        cart = request.session.get('cart', {})

        # Debugging: Print the current cart contents before modification
        print("Current Cart Contents Before Modification:", cart)

        if size:  # If the product has a size
            if str(item_id) not in cart:
                cart[str(item_id)] = {'items_by_size': {}}  # Initialize items_by_size if the item_id is not in the cart

            items_by_size = cart[str(item_id)].setdefault('items_by_size', {})
            if size in items_by_size:
                items_by_size[size] += quantity
                messages.success(request, f'Updated {product.name} (size {size}) quantity to {items_by_size[size]}!')
            else:
                items_by_size[size] = quantity
                messages.success(request, f'Added {product.name} (size {size}) to your cart!')
        else:  # If the product does not have a size
            if str(item_id) in cart:
                if 'quantity' in cart[str(item_id)]:
                    cart[str(item_id)]['quantity'] += quantity
                    messages.success(request, f'Updated {product.name} quantity to {cart[str(item_id)]["quantity"]}!')
                else:
                    cart[str(item_id)] += quantity
                    messages.success(request, f'Updated {product.name} quantity to {cart[str(item_id)]}!')
            else:
                cart[str(item_id)] = quantity
                messages.success(request, f'Added {product.name} to your cart!')

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


class UpdateCartView(View):
    def post(self, request, item_id):
        quantity = int(request.POST.get('quantity'))

        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']

        cart = request.session.get('cart', {})

        if size:
            if str(item_id) in cart and 'items_by_size' in cart[str(item_id)] and size in cart[str(item_id)]['items_by_size']:
                if quantity > 0:
                    cart[str(item_id)]['items_by_size'][size] = quantity
                else:
                    del cart[str(item_id)]['items_by_size'][size]
                    if not cart[str(item_id)]['items_by_size']:
                        del cart[str(item_id)]
        else:
            if str(item_id) in cart:
                if quantity > 0:
                    cart[str(item_id)] = quantity
                else:
                    del cart[str(item_id)]

        request.session['cart'] = cart
        return redirect('view_cart')

        
class RemoveFromCartView(View):
    def post(self, request, item_id):
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']

        cart = request.session.get('cart', {})

        if size:
            if str(item_id) in cart and 'items_by_size' in cart[str(item_id)] and size in cart[str(item_id)]['items_by_size']:
                del cart[str(item_id)]['items_by_size'][size]
                if not cart[str(item_id)]['items_by_size']:
                    del cart[str(item_id)]
        else:
            if str(item_id) in cart:
                del cart[str(item_id)]

        request.session['cart'] = cart
        return redirect('view_cart')
