from django.contrib import admin
from .models import Customer, Order, Product


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date_created', 'write_date')
    list_display_links = ('name', 'email', 'phone',
                          'date_created', 'write_date')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'description', 'date_created', 'write_date')
    list_display_links = ('name', 'price', 'category',
                          'description', 'date_created', 'write_date')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('status', 'date_created', 'write_date')
    list_display_links = ('status', 'date_created', 'write_date')
    
