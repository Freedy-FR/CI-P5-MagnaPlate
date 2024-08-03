"""
Forms configuration for the Carousel model.
"""

from django import forms
from .models import Carousel


class CarouselForm(forms.ModelForm):
    """Form for creating and updating Carousel instances."""

    class Meta:
        model = Carousel
        fields = ['image', 'link', 'caption', 'order']
