"""
Forms for the newsletter and customer support applications.

This module defines forms for subscribing to newsletters, sending newsletter
emails, and submitting customer support inquiries.
"""

from django import forms
from .models import (
    NewsletterSubscribedInfo,
    NewsletterSendEmail,
    CustomerSupportInquiry
)


class NewsletterSubscribedInfoForm(forms.ModelForm):
    """
    Form for subscribing to the newsletter.
    """
    class Meta:
        model = NewsletterSubscribedInfo
        fields = ['name', 'email']


class NewsletterSendEmailForm(forms.ModelForm):
    """
    Form for sending a newsletter email.
    """
    recipients = forms.ModelMultipleChoiceField(
        queryset=NewsletterSubscribedInfo.objects.all(),
        required=False,
        label="Recipients"
    )

    class Meta:
        model = NewsletterSendEmail
        fields = ['subject', 'body', 'send_now', 'recipients']

    def __init__(self, *args, **kwargs):
        """
        Initialize the form with selected recipients if editing an
        existing newsletter.
        """
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['recipients'].initial = self.instance.recipients.all()
        else:
            self.fields['recipients'].initial = []


class NewsletterSendForm(forms.Form):
    """
    Form for selecting newsletters to send.
    """
    newsletters = forms.ModelMultipleChoiceField(
        queryset=NewsletterSendEmail.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Select Newsletters to Send"
    )


class CustomerSupportForm(forms.ModelForm):
    """
    Form for submitting a customer support inquiry.
    """
    class Meta:
        model = CustomerSupportInquiry
        fields = [
            'name', 'email', 'subject', 'message', 'enquiry_type',
            'order_number'
        ]
