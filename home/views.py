from django.shortcuts import render
from django.views import View

class IndexView(View):
    """ A view to return the index page """

    def get(self, request):
        return render(request, 'home/index.html')
