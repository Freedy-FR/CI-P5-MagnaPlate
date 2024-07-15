from django import forms
from .models import Carousel

class CarouselForm(forms.ModelForm):
    class Meta:
        model = Carousel
        fields = ['image', 'link', 'caption', 'order']