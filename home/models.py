"""
Models configuration for the Carousel model.
"""

import os
from django.db import models


class Carousel(models.Model):
    """Model representing a carousel item."""

    image = models.ImageField(upload_to='carousel_images/')
    link = models.URLField(max_length=200, blank=True)
    caption = models.CharField(max_length=100, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Carousel item {self.id} - {self.caption}"

    def save(self, *args, **kwargs):
        """
        Save the Carousel instance, deleting the old image if it is being
        changed.
        """
        if self.pk:
            try:
                old_instance = Carousel.objects.get(pk=self.pk)
                if old_instance.image != self.image:
                    if os.path.isfile(old_instance.image.path):
                        os.remove(old_instance.image.path)
            except Carousel.DoesNotExist:
                pass
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """
        Delete the Carousel instance and its image file.
        """
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)
