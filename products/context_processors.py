from .models import Product, Collection, Creator, Category

def global_collections_and_creators(request):
    collections = Collection.objects.all()
    creators = Creator.objects.all()
    categories = Category.objects.all()
    return {
        'collections': collections,
        'creators': creators,
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