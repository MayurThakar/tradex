from .models import Product


class Main():
    def __init__(self, request):
        self.request = request

    def fetch(self):
        return Product.objects.all()
