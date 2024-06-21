from django.urls import path
from product.apps import ProductConfig

from product.views import index, product_detail

app_name = ProductConfig.name

urlpatterns = [
    path('', index, name='product_sample'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    ]
