from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def home_view(request):
    return render(request, 'accounts/dashboard.html')


def product_view(request):
    product_objs = Product.objects.all()
    context = {
        "product_objs": product_objs,
    }
    return render(request, 'accounts/products.html', context=context)


def customer_view(request):
    return render(request, 'accounts/customer.html')
