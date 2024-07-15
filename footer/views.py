from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import NewsletterEmailList, NewsletterSubscription
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import NewsletterEmailListForm, NewsletterSendForm

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
        plain_message = strip_tags(body)
        from_email = settings.DEFAULT_FROM_EMAIL
        to = subscription.email

        try:
            send_mail(subject, plain_message, from_email, [to], html_message=body)
        except BadHeaderError:
            messages.error(request, "Invalid header found.")
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")


class CreateNewsletterEmailView(View):
    def get(self, request):
        form = NewsletterEmailListForm()
        return render(request, 'newsletter_management/create_newsletter.html', {'form': form})

    def post(self, request):
        form = NewsletterEmailListForm(request.POST)
        if form.is_valid():
            newsletter = form.save(commit=False)
            recipients = form.cleaned_data['recipients']
            newsletter.save()

            if newsletter.send_now:
                self.send_newsletter(request, newsletter, recipients)
                messages.success(request, 'Newsletter sent successfully.')
            else:
                messages.success(request, 'Newsletter saved successfully and will be sent later.')
            return redirect('site_management')
        return render(request, 'newsletter_management/create_newsletter.html', {'form': form})

    def send_newsletter(self, request, newsletter, recipients):
        subject = newsletter.subject
        message = newsletter.body
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_emails = [recipient.email for recipient in recipients]

        if recipient_emails:
            try:
                send_mail(subject, message, from_email, recipient_emails)
            except Exception as e:
                messages.error(request, f"An error occurred: {e}")

class SendNewslettersView(View):
    def get(self, request):
        form = NewsletterSendForm()
        return render(request, 'newsletter_management/send_newsletters.html', {'form': form})

    def post(self, request):
        form = NewsletterSendForm(request.POST)
        if form.is_valid():
            newsletters = form.cleaned_data['newsletters']
            for newsletter in newsletters:
                self.send_newsletter(request, newsletter)
            messages.success(request, 'Selected newsletters have been sent successfully.')
            return redirect('site_management')
        return render(request, 'newsletter_management/send_newsletters.html', {'form': form})

    def send_newsletter(self, request, newsletter):
        subject = newsletter.subject
        message = newsletter.body
        from_email = settings.DEFAULT_FROM_EMAIL
        recipients = list(NewsletterSubscription.objects.values_list('email', flat=True))

        if recipients:
            try:
                send_mail(subject, message, from_email, recipients)
            except Exception as e:
                messages.error(request, f"An error occurred: {e}")