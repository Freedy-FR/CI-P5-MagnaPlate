"""
Admin configuration for the UserProfile model.
"""

from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin view for managing UserProfile instances.
    """
    list_display = (
        'user',
        'default_contact_full_name',
        'default_contact_email',
        'default_contact_phone_number'
    )
    search_fields = (
        'user__username',
        'default_contact_full_name',
        'default_contact_email',
        'default_contact_phone_number'
    )
