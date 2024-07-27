"""
Admin configuration for the orders application.

This module defines the admin interface for the Order and OrderLineItem models.
"""

from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Inline admin configuration for the OrderLineItem model.
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Order model.
    """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        'get_username', 'order_number', 'date', 'delivery_cost',
        'order_total', 'grand_total', 'original_cart', 'stripe_pid'
    )

    fields = (
        'get_username', 'order_number', 'date', 'full_name', 'email',
        'delivery_phone_number', 'country', 'postcode', 'town_or_city',
        'street_address1', 'street_address2', 'county',
        'delivery_cost', 'order_total', 'grand_total',
        'original_cart', 'stripe_pid'
    )

    list_display = (
        'get_username', 'order_number', 'date', 'full_name',
        'order_total', 'delivery_cost', 'grand_total'
    )

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
