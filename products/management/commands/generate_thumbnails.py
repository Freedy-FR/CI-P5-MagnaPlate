from django.core.management.base import BaseCommand
from easy_thumbnails.files import get_thumbnailer
from products.models import Product

class Command(BaseCommand):
    help = 'Generate thumbnails for all products'

    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        for product in products:
            if product.image and not product.thumbnail:
                thumbnailer = get_thumbnailer(product.image)
                thumbnail_options = {'size': (300, 300), 'crop': True, 'quality': 80}
                thumb = thumbnailer.get_thumbnail(thumbnail_options)
                product.thumbnail.name = thumb.name
                product.save()
        self.stdout.write(self.style.SUCCESS('Successfully generated thumbnails for all products.'))
