"""
Admin configuration for the newsletter and customer support applications.

This module registers the NewsletterSubscribedInfo, NewsletterSendEmail,
and CustomerSupportInquiry models with the Django admin site and customizes
their admin interfaces.
"""

from django.contrib import admin
from .models import (
    NewsletterSubscribedInfo,
    NewsletterSendEmail,
    CustomerSupportInquiry
)


class NewsletterSubscribedInfoAdmin(admin.ModelAdmin):
    """
    Admin configuration for the NewsletterSubscribedInfo model.
    """
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)


class NewsletterSendEmailAdmin(admin.ModelAdmin):
    """
    Admin configuration for the NewsletterSendEmail model.
    """
    list_display = ('subject', 'created_at', 'send_now')
    search_fields = ('subject',)
    filter_horizontal = ('recipients',)


class CustomerSupportInquiryAdmin(admin.ModelAdmin):
    """
    Admin configuration for the CustomerSupportInquiry model.
    """
    list_display = (
        'name', 'email', 'subject', 'enquiry_type', 'order_number',
        'ticket_number', 'created_at'
    )
    search_fields = (
        'name', 'email', 'subject', 'enquiry_type', 'order_number',
        'ticket_number'
    )
    list_filter = ('enquiry_type', 'created_at')
    readonly_fields = ('ticket_number',)


# Register the models with the admin site
admin.site.register(NewsletterSubscribedInfo, NewsletterSubscribedInfoAdmin)
admin.site.register(NewsletterSendEmail, NewsletterSendEmailAdmin)
admin.site.register(CustomerSupportInquiry, CustomerSupportInquiryAdmin)
