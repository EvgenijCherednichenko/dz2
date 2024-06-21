from django.shortcuts import render, get_object_or_404

from product.models import Product


def index(request):
    product = Product.objects.all()
    context = {"product": product}
    return render(request, 'product_sample.html', context)


def product_detail(request, pk):
    prod = get_object_or_404(Product, pk=pk)
    context = {"prod": prod}
    return render(request, 'product_detail.html', context)


