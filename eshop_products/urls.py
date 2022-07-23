from django.urls import path

from .views import ProductsList, product_detail, SearchProductsview, ProductsListByCategory, products_categories_partial

urlpatterns = [
    path('products', ProductsList.as_view()),
    path('products/<category_name>', ProductsListByCategory.as_view()),
    path('products/<productid>/<name>', product_detail),
    path('products/search', SearchProductsview.as_view()),
    path('product_categories_partial', products_categories_partial, name='products_categories_partial'),

]
