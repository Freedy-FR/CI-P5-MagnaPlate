"""
Retrieve the contents of the shopping cart from the session and
calculate totals.

This module defines a function to fetch the cart items, calculate
the total cost,
product count, delivery cost, amount needed for free delivery,
free delivery limit,
and grand total for the cart application.
"""

from decimal import Decimal

from django.conf import settings
from django.shortcuts import get_object_or_404

from products.models import Product


def cart_contents(request):
    """
    Retrieve the contents of the shopping cart from the session and calculate
    totals.

    Args:
        request: The HTTP request object.

    Returns:
        dict: A dictionary containing cart items, total cost, product count,
              delivery cost, amount needed for free delivery, free delivery
              limit,
              and grand total.
    """
    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        if isinstance(item_data, int):
            subtotal = item_data * product.price
            total += subtotal
            product_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
                'subtotal': subtotal,
            })
        else:
            for size, quantity in item_data['items_by_size'].items():
                subtotal = quantity * product.price
                total += subtotal
                product_count += quantity
                cart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                    'subtotal': subtotal,
                })

    if total < settings.FREE_DELIVERY_LIMIT:
        delivery = total * Decimal(settings.DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_LIMIT - total
    else:
        delivery = Decimal(0)
        free_delivery_delta = Decimal(0)

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_limit': settings.FREE_DELIVERY_LIMIT,
        'grand_total': grand_total,
    }

    return context
