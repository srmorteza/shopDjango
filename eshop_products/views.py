from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
from eshop_products.models import Product


def products(request):
    context = {}
    return render(request, 'products/products_list.html', context)


class ProductsList(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 1

    def get_queryset(self):
        return Product.objects.get_active_products()
