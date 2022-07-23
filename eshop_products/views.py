from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
from eshop_products.models import Product
from eshop_products_category.models import ProductsCategory


class ProductsList(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 3

    def get_queryset(self):
        return Product.objects.get_active_products()


class ProductsListByCategory(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 3

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        category = ProductsCategory.objects.filter(name__iexact=category_name).first()
        if category is None:
            raise Http404('صفحه مورد نظر یافت نشد')
        return Product.objects.get_product_by_category(category_name)


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
            return Product.objects.search(query)

        return Product.objects.get_active_products()


def products_categories_partial(request):
    categories=ProductsCategory.objects.all()
    context = {
        'categories':categories
    }
    return render(request, 'products/products_categories_partial.html', context)
