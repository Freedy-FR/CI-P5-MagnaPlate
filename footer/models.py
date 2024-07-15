from django.db import models
from django.utils import timezone

class NewsletterSubscription(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email

class NewsletterEmailList(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    send_now = models.BooleanField(default=False)

    def __str__(self):
        return self.subject
