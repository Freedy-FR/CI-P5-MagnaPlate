from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import NewsletterSendEmail, NewsletterSubscribedInfo
from .forms import NewsletterSendEmailForm, NewsletterSendForm, NewsletterSubscribedInfoForm
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.utils.html import strip_tags

class NewsletterSubscriptionView(View):
    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')

        if name and email:
            if NewsletterSubscribedInfo.objects.filter(email=email).exists():
                messages.warning(request, 'This email is already subscribed to the newsletter.')
            else:
                subscription = NewsletterSubscribedInfo(name=name, email=email)
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
        form = NewsletterSendEmailForm()
        available_recipients = NewsletterSubscribedInfo.objects.all()
        return render(request, 'newsletter_management/create_newsletter.html', {
            'form': form,
            'available_recipients': available_recipients,
            'chosen_recipients': []
        })

    def post(self, request):
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
                messages.success(request, 'Newsletter saved successfully and will be sent later.')
            return redirect('site_management')
        available_recipients = NewsletterSubscribedInfo.objects.all()
        return render(request, 'newsletter_management/create_newsletter.html', {
            'form': form,
            'available_recipients': available_recipients,
            'chosen_recipients': form.cleaned_data.get('recipients', [])
        })

    def send_newsletter(self, request, newsletter, recipients):
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


class EditNewsletterView(View):
    def get(self, request, pk):
        newsletter = get_object_or_404(NewsletterSendEmail, pk=pk)
        form = NewsletterSendEmailForm(instance=newsletter)
        available_recipients = NewsletterSubscribedInfo.objects.exclude(id__in=newsletter.recipients.values_list('id', flat=True))
        return render(request, 'newsletter_management/edit_newsletter.html', {
            'form': form, 
            'newsletter': newsletter, 
            'available_recipients': available_recipients, 
            'chosen_recipients': newsletter.recipients.all()
        })

    def post(self, request, pk):
        newsletter = get_object_or_404(NewsletterSendEmail, pk=pk)
        form = NewsletterSendEmailForm(request.POST, instance=newsletter)
        if form.is_valid():
            newsletter = form.save(commit=False)
            newsletter.save()
            form.save_m2m()
            chosen_recipients = request.POST.getlist('recipients')
            newsletter.recipients.set(chosen_recipients)

            if newsletter.send_now:
                self.send_newsletter(request, newsletter, chosen_recipients)
                messages.success(request, 'Newsletter updated and sent successfully.')
            else:
                messages.success(request, 'Newsletter updated successfully.')
            return redirect('send_newsletters')
        return render(request, 'newsletter_management/edit_newsletter.html', {'form': form, 'newsletter': newsletter})




class SendNewslettersView(View):
    def get(self, request):
        form = NewsletterSendForm()
        return render(request, 'newsletter_management/send_newsletters.html', {'form': form})

    def post(self, request):
        if 'send_selected' in request.POST:
            form = NewsletterSendForm(request.POST)
            if form.is_valid():
                newsletters = form.cleaned_data['newsletters']
                for newsletter in newsletters:
                    self.send_newsletter(request, newsletter)
                messages.success(request, 'Selected newsletters have been sent successfully.')
            return redirect('send_newsletters')

        elif 'delete_selected' in request.POST:
            selected_newsletter_ids = request.POST.getlist('newsletters')
            NewsletterSendEmail.objects.filter(id__in=selected_newsletter_ids).delete()
            messages.success(request, 'Selected newsletters have been deleted successfully.')
            return redirect('send_newsletters')

        return render(request, 'newsletter_management/send_newsletters.html', {'form': form})

    def send_newsletter(self, request, newsletter):
        subject = newsletter.subject
        message = newsletter.body
        from_email = settings.DEFAULT_FROM_EMAIL
        recipients = list(NewsletterSubscribedInfo.objects.values_list('email', flat=True))

        if recipients:
            try:
                send_mail(subject, message, from_email, recipients)
                newsletter.letter_sent = True  # Update the letter_sent field
                newsletter.save()
            except Exception as e:
                messages.error(request, f"An error occurred: {e}")

