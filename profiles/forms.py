"""
Forms for the UserProfile model.
"""

from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    Form for managing user profile information.
    """

    class Meta:
        model = UserProfile
        fields = (
            'default_contact_full_name', 'default_contact_email',
            'default_contact_phone_number', 'default_delivery_phone_number',
            'default_country', 'default_postcode', 'default_town_or_city',
            'default_street_address1', 'default_street_address2',
            'default_county'
        )

    def __init__(self, *args, **kwargs):
        """
        Initialize the form with custom placeholders and classes.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_contact_full_name': 'Full Name',
            'default_contact_email': 'Email Address',
            'default_contact_phone_number': 'Contact Phone Number',
            'default_delivery_phone_number': 'Delivery Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_contact_full_name'].widget.attrs[
            'autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'rounded-pill my-2'
            self.fields[field].label = False

        if 'class' in self.fields['default_country'].widget.attrs:
            self.fields['default_country'].widget.attrs[
                'class'] += ' select-wrapper'
        else:
            self.fields['default_country'].widget.attrs[
                'class'] = 'select-wrapper'
