from django import forms
from .models import NewsletterSubscribedInfo, NewsletterSendEmail, CustomerSupportInquiry

class NewsletterSubscribedInfoForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscribedInfo
        fields = ['name', 'email']

class NewsletterSendEmailForm(forms.ModelForm):
    recipients = forms.ModelMultipleChoiceField(
        queryset=NewsletterSubscribedInfo.objects.all(),
        required=False,
        label="Recipients"
    )

    class Meta:
        model = NewsletterSendEmail
        fields = ['subject', 'body', 'send_now', 'recipients']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['recipients'].initial = self.instance.recipients.all()
        else:
            self.fields['recipients'].initial = []


class NewsletterSendForm(forms.Form):
    newsletters = forms.ModelMultipleChoiceField(
        queryset=NewsletterSendEmail.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Select Newsletters to Send"
    )


class CustomerSupportForm(forms.ModelForm):
    class Meta:
        model = CustomerSupportInquiry
        fields = ['name', 'email', 'subject', 'message', 'enquiry_type', 'order_number']