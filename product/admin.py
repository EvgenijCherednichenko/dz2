from django.contrib import admin
from product.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", 'name')
    search_fields = ('name',)
