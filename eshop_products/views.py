from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
from eshop_products.models import Product


class ProductsList(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 3

    def get_queryset(self):
        return Product.objects.get_active_products()


def product_detail(request, *args, **kwargs):
    product_id = kwargs['productid']
    product_name = kwargs['name']
    product = Product.objects.get_by_id(product_id)
    if product is None or not product.active:
        raise Http404('محصول مورد نظر یافت نشد')
    context = {
        'product': product
    }
    return render(request, 'products/product_detail.html', context)


class SearchProductsview(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 3

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return Product.objects.filter(active=True, title__icontains=query)

        return Product.objects.get_active_products()
