from django.contrib import admin

from .models import ProductsCategory


# Register your models here.


class ProductCategoryAmin(admin.ModelAdmin):
    list_display = ['__str__', 'name']

    class Meta:
        model = ProductsCategory

admin.site.register(ProductsCategory,ProductCategoryAmin)