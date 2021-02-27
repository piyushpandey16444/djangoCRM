from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    return HttpResponse("Home Page")


def product_view(request):
    return HttpResponse("Products Page")


def customer_view(request):
    return HttpResponse("Customer Page")
