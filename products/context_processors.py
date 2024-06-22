from .models import Collection, Creator

def global_collections_and_creators(request):
    collections = Collection.objects.all()
    creators = Creator.objects.all()
    return {
        'collections': collections,
        'creators': creators,
    }

def sorting_options(request):
    sort_options = [
        {'label': 'By Price', 'value': 'price'},
        {'label': 'By Rating', 'value': '-rating'},
        {'label': 'By Category', 'value': 'category'},
        {'label': 'By Name', 'value': 'name'},
    ]
    return {'sort_options': sort_options}
