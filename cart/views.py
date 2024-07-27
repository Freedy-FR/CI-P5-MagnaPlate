"""
Views for the cart application.

This module defines views for viewing, adding to, updating, and removing
from the cart.
"""

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import TemplateView

from cart.contexts import cart_contents  # Import the cart_contents function
from products.models import Product


class ViewCart(TemplateView):
    """
    View to display the contents of the cart.
    """
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        """
        Get the context data for the cart view.

        Returns:
            dict: Context data for the template.
        """
        context = super().get_context_data(**kwargs)
        return context


class AddToCartView(View):
    """
    Add a quantity of the specified product to the shopping cart.
    """

    def post(self, request, item_id):
        """
        Handle POST request to add a product to the cart.

        Args:
            request: The HTTP request object.
            item_id (int): The ID of the product to add.

        Returns:
            HttpResponse: Redirect to the specified URL.
        """
        try:
            quantity = int(request.POST.get('quantity'))
            redirect_url = request.POST.get('redirect_url')
            product = get_object_or_404(Product, pk=item_id)

            size = request.POST.get('product_size', None)
            cart = request.session.get('cart', {})

            if size:  # If the product has a size
                if str(item_id) not in cart:
                    cart[str(item_id)] = {'items_by_size': {}}

                items_by_size = cart[str(item_id)].setdefault(
                    'items_by_size', {}
                )
                if size in items_by_size:
                    items_by_size[size] += quantity
                    messages.success(
                        request,
                        f'Updated {product.name} (size {size}) quantity '
                        f'to {items_by_size[size]}!'
                    )
                else:
                    items_by_size[size] = quantity
                    messages.success(
                        request,
                        f'Added {product.name} (size {size}) to your cart!'
                    )
            else:  # If the product does not have a size
                if str(item_id) in cart:
                    if 'quantity' in cart[str(item_id)]:
                        cart[str(item_id)]['quantity'] += quantity
                        messages.success(
                            request,
                            f'Updated {product.name} quantity to '
                            f'{cart[str(item_id)]["quantity"]}!'
                        )
                    else:
                        cart[str(item_id)] += quantity
                        messages.success(
                            request,
                            f'Updated {product.name} quantity to '
                            f'{cart[str(item_id)]}!'
                        )
                else:
                    cart[str(item_id)] = quantity
                    messages.success(
                        request,
                        f'Added {product.name} to your cart!'
                    )

            request.session['cart'] = cart
            return redirect(redirect_url)
        except Exception as e:
            messages.error(
                request,
                f'Error adding item to cart: {str(e)}'
            )
            return redirect(redirect_url)


class UpdateCartView(View):
    """
    Update the quantity of a specified product in the shopping cart.
    """

    def post(self, request, item_id):
        """
        Handle POST request to update a product in the cart.

        Args:
            request: The HTTP request object.
            item_id (int): The ID of the product to update.

        Returns:
            HttpResponse: Redirect to the cart view.
        """
        try:
            quantity = int(request.POST.get('quantity'))
            product = get_object_or_404(Product, pk=item_id)

            size = request.POST.get('product_size', None)
            cart = request.session.get('cart', {})

            if size:
                if (str(item_id) in cart and
                        'items_by_size' in cart[str(item_id)] and
                        size in cart[str(item_id)]['items_by_size']):
                    if quantity > 0:
                        cart[str(item_id)]['items_by_size'][size] = quantity
                        messages.success(
                            request,
                            f'Updated {product.name} (size {size}) quantity '
                            f'to {quantity}!'
                        )
                    else:
                        del cart[str(item_id)]['items_by_size'][size]
                        if not cart[str(item_id)]['items_by_size']:
                            del cart[str(item_id)]
                            messages.success(
                                request,
                                f'Removed {product.name} (size {size}) '
                                f'from your cart!'
                            )
            else:
                if str(item_id) in cart:
                    if quantity > 0:
                        cart[str(item_id)] = quantity
                        messages.success(
                            request,
                            f'Updated {product.name} quantity to {quantity}!'
                        )
                    else:
                        del cart[str(item_id)]
                        messages.success(
                            request,
                            f'Removed {product.name} from your cart!'
                        )

            request.session['cart'] = cart
            return redirect('view_cart')
        except Exception as e:
            messages.error(
                request,
                f'Error updating cart: {str(e)}'
            )
            return redirect('view_cart')


class RemoveFromCartView(View):
    """
    Remove a specified product from the shopping cart.
    """

    def post(self, request, item_id):
        """
        Handle POST request to remove a product from the cart.

        Args:
            request: The HTTP request object.
            item_id (int): The ID of the product to remove.

        Returns:
            HttpResponse: Redirect to the cart view.
        """
        try:
            size = request.POST.get('product_size', None)
            cart = request.session.get('cart', {})
            product = get_object_or_404(Product, pk=item_id)

            if size:
                if (str(item_id) in cart and
                        'items_by_size' in cart[str(item_id)] and
                        size in cart[str(item_id)]['items_by_size']):
                    del cart[str(item_id)]['items_by_size'][size]
                    if not cart[str(item_id)]['items_by_size']:
                        del cart[str(item_id)]
                    messages.success(
                        request,
                        f'Removed {product.name} (size {size}) from your cart!'
                    )
            else:
                if str(item_id) in cart:
                    del cart[str(item_id)]
                messages.success(
                    request,
                    f'Removed {product.name} from your cart!'
                )

            request.session['cart'] = cart
            return redirect('view_cart')
        except Exception as e:
            messages.error(
                request,
                f'Error removing item from cart: {str(e)}'
            )
            return redirect('view_cart')
