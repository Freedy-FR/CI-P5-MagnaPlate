from django.db import models
from django.utils import timezone

class NewsletterSubscription(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email
