"""
This module contains views for managing newsletters, subscriptions,
and customer support in a Django web application.
"""

from itertools import groupby

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)
from django.core.mail import send_mail, BadHeaderError
from django.db.models import Subquery, F, Q
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.html import strip_tags
from django.views import View
from django.views.generic import TemplateView, ListView, DeleteView
from django.views.generic.detail import DetailView

from .forms import (
    NewsletterSendEmailForm, NewsletterSendForm,
    NewsletterSubscribedInfoForm, CustomerSupportForm
)
from .models import (
    NewsletterSendEmail, NewsletterSubscribedInfo,
    CustomerSupportInquiry
)


class NewsletterSubscriptionView(View):
    """View to handle newsletter subscriptions."""

    def post(self, request):
        """
        Handle POST requests to subscribe to the newsletter.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: Redirects to the home page.
        """
        name = request.POST.get('name')
        email = request.POST.get('email')

        if name and email:
            if NewsletterSubscribedInfo.objects.filter(email=email).exists():
                messages.warning(
                    request,
                    'This email is already subscribed to the newsletter.'
                )
            else:
                subscription = NewsletterSubscribedInfo(name=name, email=email)
                subscription.save()
                self.send_confirmation_email(request, subscription)
                messages.success(
                    request,
                    'You have successfully subscribed to the newsletter.'
                )
        else:
            messages.error(
                request,
                'There was an error with your submission. '
                'Please check the form and try again.'
            )

        return redirect('home')

    def send_confirmation_email(self, request, subscription):
        """
        Send a confirmation email to the new subscriber.

        Args:
            request (HttpRequest): The HTTP request object.
            subscription (NewsletterSubscribedInfo): The subscription object.
        """
        subject = 'Subscription Confirmation'
        body = render_to_string(
            'footer/emails/subscription_confirmation.html',
            {'name': subscription.name}
        )
        plain_message = strip_tags(body)
        from_email = settings.DEFAULT_FROM_EMAIL
        to = subscription.email

        try:
            send_mail(
                subject, plain_message, from_email, [to], html_message=body
            )
        except BadHeaderError:
            messages.error(request, "Invalid header found.")
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")


class AdminOrSuperuserRequiredMixin(UserPassesTestMixin):
    """Mixin to allow only admin or superuser access."""

    def test_func(self):
        """
        Test if the user is an admin or superuser.

        Returns:
            bool: True if the user is superuser or staff.
        """
        return self.request.user.is_superuser or self.request.user.is_staff


class CreateNewsletterEmailView(
    LoginRequiredMixin, AdminOrSuperuserRequiredMixin, View
):
    """View to create a new newsletter email."""

    def get(self, request):
        """
        Handle GET requests to display the newsletter creation form.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: Renders the create newsletter template.
        """
        form = NewsletterSendEmailForm()
        available_recipients = NewsletterSubscribedInfo.objects.all()
        return render(
            request,
            'newsletter_management/create_newsletter.html',
            {
                'form': form,
                'available_recipients': available_recipients,
                'chosen_recipients': []
            }
        )

    def post(self, request):
        """
        Handle POST requests to create a new newsletter email.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: Redirects to the site management page.
        """
        form = NewsletterSendEmailForm(request.POST)
        if form.is_valid():
            newsletter = form.save(commit=False)
            newsletter.save()
            form.save_m2m()  # Save the many-to-many relationships

            recipients = form.cleaned_data['recipients']
            if newsletter.send_now:
                self.send_newsletter(request, newsletter, recipients)
                messages.success(request, 'Newsletter sent successfully.')
            else:
                messages.success(
                    request,
                    'Newsletter saved successfully and will be sent later.'
                )
            return redirect('site_management')
        available_recipients = NewsletterSubscribedInfo.objects.all()
        return render(
            request,
            'newsletter_management/create_newsletter.html',
            {
                'form': form,
                'available_recipients': available_recipients,
                'chosen_recipients': form.cleaned_data.get('recipients', [])
            }
        )

    def send_newsletter(self, request, newsletter, recipients):
        """
        Send the newsletter to the specified recipients.

        Args:
            request (HttpRequest): The HTTP request object.
            newsletter (NewsletterSendEmail): The newsletter object.
            recipients (QuerySet): The recipients of the newsletter.
        """
        subject = newsletter.subject
        message = newsletter.body
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_emails = [recipient.email for recipient in recipients]

        if recipient_emails:
            try:
                send_mail(subject, message, from_email, recipient_emails)
                newsletter.letter_sent = True
                newsletter.save()
            except Exception as e:
                messages.error(request, f"An error occurred: {e}")


class EditNewsletterView(
    LoginRequiredMixin, AdminOrSuperuserRequiredMixin, View
):
    """View to edit an existing newsletter email."""

    def get(self, request, pk):
        """
        Handle GET requests to display the newsletter editing form.

        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): Primary key of the newsletter to edit.

        Returns:
            HttpResponse: Renders the edit newsletter template.
        """
        newsletter = get_object_or_404(NewsletterSendEmail, pk=pk)
        form = NewsletterSendEmailForm(instance=newsletter)
        available_recipients = NewsletterSubscribedInfo.objects.exclude(
            id__in=newsletter.recipients.values_list('id', flat=True)
        )
        return render(
            request,
            'newsletter_management/edit_newsletter.html',
            {
                'form': form,
                'newsletter': newsletter,
                'available_recipients': available_recipients,
                'chosen_recipients': newsletter.recipients.all()
            }
        )

    def post(self, request, pk):
        """
        Handle POST requests to update an existing newsletter email.

        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): Primary key of the newsletter to edit.

        Returns:
            HttpResponse: Redirects to the send newsletters page.
        """
        newsletter = get_object_or_404(NewsletterSendEmail, pk=pk)
        form = NewsletterSendEmailForm(request.POST, instance=newsletter)
        if form.is_valid():
            newsletter = form.save(commit=False)
            newsletter.save()
            form.save_m2m()
            chosen_recipient_ids = request.POST.getlist('recipients')
            chosen_recipients = NewsletterSubscribedInfo.objects.filter(
                id__in=chosen_recipient_ids
            )
            newsletter.recipients.set(chosen_recipients)

            if newsletter.send_now:
                self.send_newsletter(request, newsletter, chosen_recipients)
                messages.success(
                    request,
                    'Newsletter updated and sent successfully.'
                )
            else:
                messages.success(request, 'Newsletter updated successfully.')
            return redirect('send_newsletters')
        return render(
            request,
            'newsletter_management/edit_newsletter.html',
            {'form': form, 'newsletter': newsletter}
        )

    def send_newsletter(self, request, newsletter, recipients):
        """
        Send the updated newsletter to the specified recipients.

        Args:
            request (HttpRequest): The HTTP request object.
            newsletter (NewsletterSendEmail): The newsletter object.
            recipients (QuerySet): The recipients of the newsletter.
        """
        subject = newsletter.subject
        message = newsletter.body
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_emails = [recipient.email for recipient in recipients]

        if recipient_emails:
            try:
                send_mail(subject, message, from_email, recipient_emails)
                newsletter.letter_sent = True
                newsletter.save()
                messages.success(request, 'Newsletter sent successfully.')
            except Exception as e:
                messages.error(request, f"An error occurred: {e}")


class SendNewslettersView(
    LoginRequiredMixin, AdminOrSuperuserRequiredMixin, View
):
    """View to manage sending or deleting multiple newsletters."""

    def get(self, request):
        """
        Handle GET requests to display the send newsletters form.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: Renders the send newsletters template.
        """
        form = NewsletterSendForm()
        return render(
            request,
            'newsletter_management/send_newsletters.html',
            {'form': form}
        )

    def post(self, request):
        """
        Handle POST requests to send or delete selected newsletters.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: Redirects to the send newsletters page.
        """
        if 'send_selected' in request.POST:
            form = NewsletterSendForm(request.POST)
            if form.is_valid():
                newsletters = form.cleaned_data['newsletters']
                for newsletter in newsletters:
                    self.send_newsletter(request, newsletter)
                messages.success(
                    request,
                    'Selected newsletters have been sent successfully.'
                )
            return redirect('send_newsletters')

        elif 'delete_selected' in request.POST:
            selected_newsletter_ids = request.POST.getlist('newsletters')
            NewsletterSendEmail.objects.filter(
                id__in=selected_newsletter_ids
            ).delete()
            messages.success(
                request,
                'Selected newsletters have been deleted successfully.'
            )
            return redirect('send_newsletters')

        return render(
            request,
            'newsletter_management/send_newsletters.html',
            {'form': form}
        )

    def send_newsletter(self, request, newsletter):
        """
        Send the specified newsletter to all recipients.

        Args:
            request (HttpRequest): The HTTP request object.
            newsletter (NewsletterSendEmail): The newsletter object.
        """
        subject = newsletter.subject
        message = newsletter.body
        from_email = settings.DEFAULT_FROM_EMAIL
        recipients = list(
            NewsletterSubscribedInfo.objects.values_list('email', flat=True)
        )

        if recipients:
            try:
                send_mail(subject, message, from_email, recipients)
                newsletter.letter_sent = True  # Update the letter_sent field
                newsletter.save()
            except Exception as e:
                messages.error(request, f"An error occurred: {e}")


# Subscription Management

class SubscriptionListView(
    LoginRequiredMixin, AdminOrSuperuserRequiredMixin, ListView
):
    """View to display a list of newsletter subscriptions."""

    model = NewsletterSubscribedInfo
    template_name = 'newsletter_management/subscription_list.html'
    context_object_name = 'subscriptions'

    def get_queryset(self):
        """
        Get the list of subscriptions, filtered by search term if provided.

        Returns:
            QuerySet: The filtered list of subscriptions.
        """
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | Q(email__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        """
        Add the search term to the context data.

        Returns:
            dict: The context data.
        """
        context = super().get_context_data(**kwargs)
        context['search_term'] = self.request.GET.get('q', '')
        return context


class SubscriptionDeleteView(
    LoginRequiredMixin, AdminOrSuperuserRequiredMixin, DeleteView
):
    """View to delete a newsletter subscription."""

    model = NewsletterSubscribedInfo
    template_name = 'newsletter_management/subscription_confirm_delete.html'
    success_url = reverse_lazy('subscription_list')

    def delete(self, request, *args, **kwargs):
        """
        Handle deletion of a subscription.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: Redirects to the subscription list page.
        """
        self.object = self.get_object()
        self.object.delete()
        messages.success(request, 'Subscription deleted successfully!')
        return redirect(self.success_url)


class AboutUsView(TemplateView):
    """View to display the 'About Us' page."""

    template_name = 'footer/about_us.html'


class FaqView(TemplateView):
    """View to display the FAQ page."""

    template_name = 'footer/faq.html'


class CustomerSupportView(View):
    """View to handle customer support inquiries."""

    def get(self, request):
        """
        Handle GET requests to display the customer support form.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: Renders the customer support form template.
        """
        form = CustomerSupportForm()
        return render(request, 'footer/customer_support.html', {'form': form})

    def post(self, request):
        """
        Handle POST requests to submit a customer support inquiry.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: Redirects to the customer support page.
        """
        form = CustomerSupportForm(request.POST)
        if form.is_valid():
            inquiry = form.save()
            messages.success(
                request,
                f'Thank you for your inquiry. '
                f'Your ticket number is {inquiry.ticket_number}. '
                'Our support team will contact you soon.'
            )
            return redirect('customer_support')
        return render(request, 'footer/customer_support.html', {'form': form})


class CustomerSupportListView(
    LoginRequiredMixin, AdminOrSuperuserRequiredMixin, ListView
):
    """View to display a list of customer support inquiries."""

    model = CustomerSupportInquiry
    template_name = 'customer_management/customer_support_list.html'
    context_object_name = 'grouped_inquiries'

    def get_queryset(self):
        """
        Get the list of customer support inquiries, grouped by type.

        Returns:
            list: The grouped list of inquiries.
        """
        # Retrieve all inquiries ordered by enquiry_type and created_at
        inquiries = CustomerSupportInquiry.objects.all().order_by(
            'enquiry_type', '-created_at'
        )

        # Group inquiries by enquiry_type
        grouped_inquiries = []
        for key, group in groupby(inquiries, key=lambda x: x.enquiry_type):
            grouped_inquiries.append({
                'enquiry_type': key,
                'inquiries': list(group)
            })

        return grouped_inquiries


class CustomerSupportDeleteView(
    LoginRequiredMixin, AdminOrSuperuserRequiredMixin, View
):
    """View to delete a customer support inquiry."""

    def post(self, request, pk, *args, **kwargs):
        """
        Handle POST requests to delete a customer support inquiry.

        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): Primary key of the inquiry to delete.

        Returns:
            HttpResponse: Redirects to the customer support list page.
        """
        inquiry = get_object_or_404(CustomerSupportInquiry, pk=pk)
        inquiry.delete()
        messages.success(
            request, 'The customer support inquiry was successfully deleted.'
        )
        return redirect('customer_support_list')


class CustomerSupportDetailView(
    LoginRequiredMixin, AdminOrSuperuserRequiredMixin, DetailView
):
    """View to display the details of a customer support inquiry."""

    model = CustomerSupportInquiry
    template_name = 'customer_management/customer_support_detail.html'
    context_object_name = 'inquiry'


class ContactUsView(TemplateView):
    """View to display the 'Contact Us' page."""

    template_name = 'footer/contact_us.html'
