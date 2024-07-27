"""
Forms for the orders application.

This module defines the form for creating and updating orders.
"""

from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Form for creating and updating an order.
    """
    class Meta:
        model = Order
        fields = (
            'full_name', 'email', 'delivery_phone_number',
            'street_address1', 'street_address2',
            'town_or_city', 'postcode', 'country',
            'county',
        )

    def __init__(self, *args, **kwargs):
        """
        Initialize the form with placeholders and classes,
        remove auto-generated labels, and set autofocus on the first field.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'delivery_phone_number': 'Delivery Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
        }

        for field in self.fields:
            if field != 'country':
                placeholder = (
                    f"{placeholders[field]}"
                    f"{' *' if self.fields[field].required else ''}"
                )
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = (
                'stripe-style-input rounded-pill my-2'
            )
            self.fields[field].label = False

        if 'class' in self.fields['country'].widget.attrs:
            self.fields['country'].widget.attrs['class'] += ' select-wrapper'
        else:
            self.fields['country'].widget.attrs['class'] = ' select-wrapper'
