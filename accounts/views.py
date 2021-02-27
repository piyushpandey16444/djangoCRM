from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    return render(request, 'accounts/dashboard.html')


def product_view(request):
    return render(request, 'accounts/products.html')


def customer_view(request):
    return render(request, 'accounts/customer.html')
