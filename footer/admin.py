from django.contrib import admin
from .models import NewsletterSubscribedInfo, NewsletterSendEmail, CustomerSupportInquiry

class NewsletterSubscribedInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)

admin.site.register(NewsletterSubscribedInfo, NewsletterSubscribedInfoAdmin)

class NewsletterSendEmailAdmin(admin.ModelAdmin):
    list_display = ('subject', 'created_at', 'send_now')
    search_fields = ('subject',)
    filter_horizontal = ('recipients',)

admin.site.register(NewsletterSendEmail, NewsletterSendEmailAdmin)

class CustomerSupportInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'enquiry_type', 'order_number', 'ticket_number', 'created_at')
    search_fields = ('name', 'email', 'subject', 'enquiry_type', 'order_number', 'ticket_number')
    list_filter = ('enquiry_type', 'created_at')
    readonly_fields = ('ticket_number',)

admin.site.register(CustomerSupportInquiry, CustomerSupportInquiryAdmin)