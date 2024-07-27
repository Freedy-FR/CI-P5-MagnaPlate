"""
Models for the newsletter and customer support applications.

This module defines models for newsletter subscription information,
sending newsletter emails, and handling customer support inquiries.
"""

import uuid
from django.db import models
from django.utils import timezone


class NewsletterSubscribedInfo(models.Model):
    """
    Model representing a newsletter subscriber's information.
    """
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email


class NewsletterSendEmail(models.Model):
    """
    Model representing an email to be sent as a newsletter.
    """
    subject = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    send_now = models.BooleanField(default=False)
    recipients = models.ManyToManyField(NewsletterSubscribedInfo)
    letter_sent = models.BooleanField(default=False)

    def __str__(self):
        return self.subject


class CustomerSupportInquiry(models.Model):
    """
    Model representing a customer support inquiry.
    """
    ENQUIRY_TYPES = [
        ('order', 'Order Enquiry'),
        ('product', 'Product Enquiry'),
        ('returns', 'Returns'),
        ('complaints', 'Complaints'),
        ('work', 'Work With Us'),
        ('others', 'Others'),
        ('shipping', 'Shipping Inquiry'),
        ('payment', 'Payment Inquiry'),
        ('technical', 'Technical Support'),
        ('feedback', 'Feedback'),
        ('partnership', 'Partnership Inquiry'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    enquiry_type = models.CharField(max_length=50, choices=ENQUIRY_TYPES)
    order_number = models.CharField(max_length=50, blank=True, null=True)
    ticket_number = models.CharField(max_length=32, null=False, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def _generate_ticket_number(self):
        """
        Generate a random, unique ticket number using UUID.
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the ticket number
        if it hasn't been set already.
        """
        if not self.ticket_number:
            self.ticket_number = self._generate_ticket_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.subject
