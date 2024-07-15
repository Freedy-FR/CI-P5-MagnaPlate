from django.contrib import admin
from .models import NewsletterSubscription, NewsletterEmailList

class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)

admin.site.register(NewsletterSubscription, NewsletterSubscriptionAdmin)


@admin.register(NewsletterEmailList)
class NewsletterEmailListAdmin(admin.ModelAdmin):
    list_display = ('subject', 'created_at', 'send_now')
    search_fields = ('subject',)