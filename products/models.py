from django.db import models
from django.utils import timezone
from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.signal_handlers import generate_aliases
from easy_thumbnails.signals import saved_file

class Collection(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Collections'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    collection = models.ForeignKey('Collection', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Creator(models.Model):
    name = models.CharField(max_length=254)
    image = models.ImageField(upload_to='creator_images', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Check if the image field has a file
        if self.image:
            # Extract the file extension
            ext = self.image.name.split('.')[-1]
            # Construct the new image name
            new_image_name = f"creators-{self.name}.{ext}"
            # Set the new image name
            self.image.name = new_image_name

        super().save(*args, **kwargs)


class Product(models.Model):

    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    ]

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    collection = models.ForeignKey('Collection', null=True, blank=True, on_delete=models.SET_NULL)
    creator = models.ForeignKey('Creator', null=True, blank=True, on_delete=models.SET_NULL, related_name='products')
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    size = models.CharField(max_length=2, choices=SIZE_CHOICES, null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to='product_images', null=True, blank=True)
    thumbnail = ThumbnailerImageField(upload_to='product_thumbnails', editable=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_on_deal = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = self.generate_sku()
        
        # Generate thumbnail if image is present
        if self.image and not self.thumbnail:
            self.thumbnail.save(self.image.name, self.image)
        
        super().save(*args, **kwargs)

    def generate_sku(self):
        collection_code = self.collection.name[:3].upper() if self.collection else 'XXX'
        category_code = self.category.name[:3].upper() if self.category else 'XXX'
        unique_number = str(Product.objects.count() + 1).zfill(5)
        return f"{collection_code}-{category_code}-{unique_number}"

saved_file.connect(generate_aliases, sender=Product.image)