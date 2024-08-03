"""
This management command generates thumbnails for all products that have an
image
but do not yet have a thumbnail.

To run this command, use:
    python manage.py <command_name>
"""

from django.core.management.base import BaseCommand
from easy_thumbnails.files import get_thumbnailer
from products.models import Product


class Command(BaseCommand):
    """
    A custom management command to generate thumbnails for all products.
    """

    help = 'Generate thumbnails for all products'

    def handle(self, *args, **kwargs):
        """
        The main method that gets executed when the command is run.

        It iterates over all products, and if a product has an image but
        does not have a thumbnail, it generates a thumbnail for that product.
        """
        products = Product.objects.all()
        for product in products:
            if product.image and not product.thumbnail:
                thumbnailer = get_thumbnailer(product.image)
                thumbnail_options = {
                    'size': (300, 300), 'crop': True, 'quality': 80
                }
                thumb = thumbnailer.get_thumbnail(thumbnail_options)
                product.thumbnail.name = thumb.name
                product.save()
        self.stdout.write(
            self.style.SUCCESS(
                'Successfully generated thumbnails for all products.'
            )
        )
