from django import forms
from .models import Product, Category, Collection, Creator


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        categories = Category.objects.all()
        category_friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        collections = Collection.objects.all()
        collection_friendly_names = [(c.id, c.get_friendly_name()) for c in collections]

        self.fields['category'].choices = category_friendly_names
        self.fields['collection'].choices = collection_friendly_names

        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs['class'] = 'rounded my-2 border-black'
            elif isinstance(field.widget, forms.ClearableFileInput):
                field.widget.attrs['class'] = 'rounded my-2 border-black'
            else:
                field.widget.attrs['class'] = 'rounded-pill my-2 border-black'

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name', 'friendly_name', 'collection']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        collections = Collection.objects.all()
        collection_friendly_names = [(c.id, c.get_friendly_name()) for c in collections]

        self.fields['collection'].choices = collection_friendly_names

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded my-2 border-black'


class CollectionForm(forms.ModelForm):
    
    class Meta:
        model = Collection
        fields = ['name', 'friendly_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded my-2 border-black'

class CreatorForm(forms.ModelForm):

    class Meta:
        model = Creator
        fields = ['name', 'image', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs['class'] = 'rounded my-2 border-black'
            elif isinstance(field.widget, forms.ClearableFileInput):
                field.widget.attrs['class'] = 'rounded my-2 border-black'
            else:
                field.widget.attrs['class'] = 'rounded my-2 border-black'