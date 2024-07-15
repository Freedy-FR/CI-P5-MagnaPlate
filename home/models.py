from django.db import models
import os

class Carousel(models.Model):
    image = models.ImageField(upload_to='carousel_images/')
    link = models.URLField(max_length=200, blank=True)
    caption = models.CharField(max_length=100, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Carousel item {self.id} - {self.caption}"

    def save(self, *args, **kwargs):
        # Check if an instance with this id already exists
        if self.pk:
            try:
                old_instance = Carousel.objects.get(pk=self.pk)
                # Check if the image is being changed
                if old_instance.image != self.image:
                    # If so, delete the old image
                    if os.path.isfile(old_instance.image.path):
                        os.remove(old_instance.image.path)
            except Carousel.DoesNotExist:
                pass
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Delete the image file when the instance is deleted
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)