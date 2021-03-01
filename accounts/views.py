from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Order, Customer


def home_view(request):
    order_objs = Order.objects.all()
    customer_objs = Customer.objects.all()
    context = {
        "order_objs": order_objs,
        "customer_objs": customer_objs,
    }
    return render(request, 'accounts/dashboard.html', context=context)


def product_view(request):
    product_objs = Product.objects.all()
    context = {
        "product_objs": product_objs,
    }
    return render(request, 'accounts/products.html', context=context)


def customer_view(request):
    return render(request, 'accounts/customer.html')
