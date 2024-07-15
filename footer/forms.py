from django import forms
from .models import NewsletterSubscription, NewsletterEmailList

class NewsletterSubscriptionForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ['name', 'email']


class NewsletterEmailListForm(forms.ModelForm):
    recipients = forms.ModelMultipleChoiceField(
        queryset=NewsletterSubscription.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Recipients"
    )

    class Meta:
        model = NewsletterEmailList
        fields = ['subject', 'body', 'send_now', 'recipients']


class NewsletterSendForm(forms.Form):
    newsletters = forms.ModelMultipleChoiceField(
        queryset=NewsletterEmailList.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Select Newsletters to Send"
    )