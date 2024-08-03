"""
Context processors for including collections, creators, categories, sorting
options, and all products in the context of templates.
"""

import random
from .models import Product, Collection, Creator, Category


def global_collections_and_creators(request):
    """
    Add collections, creators, categories, and a random sample of creators to
    the context.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        dict: A dictionary with collections, creators, random creators, and
        categories.
    """
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
    """
    Add sorting options to the context.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        dict: A dictionary with sorting options.
    """
    sort_options = [
        {'label': 'By Price', 'value': 'price_asc'},
        {'label': 'By Rating', 'value': 'rating_desc'},
        {'label': 'By Category', 'value': 'category'},
        {'label': 'By Name', 'value': 'name_asc'},
    ]

    return {'sort_options': sort_options}


def all_products(request):
    """
    Add all products to the context.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        dict: A dictionary with all products.
    """
    products = Product.objects.all()

    return {'products': products}
