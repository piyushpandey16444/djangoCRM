from django.contrib import admin
from .models import Customer, Order, Product
from django.utils.html import format_html



@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('upper_case_name', 'email', 'phone',
                    'date_created', 'write_date')
    list_display_links = ('upper_case_name', 'email', 'phone',
                          'date_created', 'write_date')
    date_hierarchy = 'date_created'

    def upper_case_name(self, obj):
        return f"{(obj.name).upper()}"
    upper_case_name.short_description = 'Name Given'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'description', 'date_created', 'write_date')
    list_display_links = ('name', 'price', 'category',
                          'description', 'date_created', 'write_date')
    date_hierarchy = 'date_created'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('colored_status', 'date_created', 'write_date')
    list_display_links = ('colored_status', 'date_created', 'write_date')
    date_hierarchy = 'date_created'

    def colored_status(self, obj):
        if obj.status == 'pending':
            return format_html(
                '<span style="color: red;">{}</span>',
                (obj.status).upper(),
            )
        elif obj.status == 'out_for_delivery':
            return format_html(
                '<span style="color: blue;">{}</span>',
                (obj.status).upper(),
            )
        else:
            return format_html(
                '<span style="color: green;">{}</span>',
                (obj.status).upper(),
            )


    
