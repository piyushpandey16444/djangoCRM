from django.urls import path
from .views import home_view, product_view, customer_view

urlpatterns = [
    path('', home_view, name="home"),
    path('products/', product_view, name="product"),
    path('customer/', customer_view, name="customer"),
]
