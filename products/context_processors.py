from .models import Product, Collection, Creator, Category
import random

def global_collections_and_creators(request):
    collections = Collection.objects.all()
    creators = Creator.objects.all()
    categories = Category.objects.all()
    all_creators = list(Creator.objects.all())
    random_creators = random.sample(all_creators, min(len(all_creators), 5))
    return {
        'collections': collections,
        'creators': creators,
        'random_creators': random_creators,
        'categories': categories,
    }

def sorting_options(request):
    sort_options = [
        {'label': 'By Price', 'value': 'price_asc'},
        {'label': 'By Rating', 'value': 'rating_desc'},
        {'label': 'By Category', 'value': 'category'},
        {'label': 'By Name', 'value': 'name_asc'},
    ]
    return {'sort_options': sort_options}

def all_products(request):
    products = Product.objects.all()
    return {'products': products}
