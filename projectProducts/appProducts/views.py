from django.shortcuts import render
from appProducts.main import Main

# Create your views here.


def index(request):
    reference = Main(request)
    products = reference.fetch()
    return render(request, 'index.html', {'products': products})
