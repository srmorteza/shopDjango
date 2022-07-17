from django.urls import path

from .views import ProductsList, product_detail, SearchProductsview

urlpatterns = [
    path('products', ProductsList.as_view()),
    path('products/<productid>/<name>', product_detail),
    path('products/search', SearchProductsview.as_view()),

]
