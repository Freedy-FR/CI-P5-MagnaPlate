from django.contrib import admin
from .models import NewsletterSubscription

class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)

admin.site.register(NewsletterSubscription, NewsletterSubscriptionAdmin)