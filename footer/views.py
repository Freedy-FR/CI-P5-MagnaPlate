from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import NewsletterSubscription

from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views import View
from django.contrib import messages

from django.http import HttpResponse

class NewsletterSubscriptionView(View):
    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')

        if name and email:
            if NewsletterSubscription.objects.filter(email=email).exists():
                messages.warning(request, 'This email is already subscribed to the newsletter.')
            else:
                subscription = NewsletterSubscription(name=name, email=email)
                subscription.save()
                self.send_confirmation_email(request, subscription)
                messages.success(request, 'You have successfully subscribed to the newsletter.')
        else:
            messages.error(request, 'There was an error with your submission. Please check the form and try again.')

        return redirect('home')

    def send_confirmation_email(self, request, subscription):
        subject = 'Subscription Confirmation'
        body = render_to_string('footer/emails/subscription_confirmation.html', {'name': subscription.name})
        from_email = settings.DEFAULT_FROM_EMAIL
        to = subscription.email

        try:
            send_mail(subject, body, from_email, [to])
            print("Email sent successfully")  # Add this line for debugging
        except BadHeaderError:
            messages.error(request, "Invalid header found.")
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            print(f"An error occurred: {e}")  # Add this line for debugging
