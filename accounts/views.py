from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Order, Customer


def home_view(request):
    
    order_objs = Order.objects.all()
    customer_objs = Customer.objects.all()
    total_customers = customer_objs.count()
    total_orders = order_objs.count()
    delivered_orders = order_objs.filter(status="delivered").count()
    pending_orders = order_objs.filter(status="pending").count()

    context = {
        "order_objs": order_objs,
        "customer_objs": customer_objs,
        "total_customers": total_customers,
        "total_orders": total_orders,
        "delivered_orders": delivered_orders,
        "pending_orders": pending_orders,

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
