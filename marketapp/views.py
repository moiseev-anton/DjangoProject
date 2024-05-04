from django.shortcuts import render

from .models import Product


def home(request):
    return render(request, 'marketapp/base.html')


def about(request):
    return render(request, 'marketapp/about.html')


def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'marketapp/products.html', context)
