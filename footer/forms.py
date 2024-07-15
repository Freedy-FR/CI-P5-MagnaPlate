from django import forms
from .models import NewsletterSubscription

class NewsletterSubscriptionForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ['name', 'email']
