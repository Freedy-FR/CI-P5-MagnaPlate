"""
Template tags and filters for the cart application.

This module defines custom template
filters for use in the cart application templates.
"""

from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    Calculate the subtotal for a given price and quantity.

    Args:
        price (Decimal): The price of the product.
        quantity (int): The quantity of the product.

    Returns:
        Decimal: The subtotal for the given price and quantity.
    """
    return price * quantity
