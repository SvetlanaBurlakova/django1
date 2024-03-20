from django.contrib import admin

from .models import Client, Product, Order


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address', 'registration_date']
    ordering = ['name']
    list_filter = ['registration_date']
    search_fields = ['email']
    search_help_text = 'Поиск по полю электронная почта (email)'


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'count', 'date_added', 'image']
    ordering = ['name', 'count']
    list_filter = ['count', 'name', 'date_added']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'get_products', 'total_price', 'date_ordered']
    ordering = ['-date_ordered']
    list_filter = ['client', 'products', 'date_ordered']
    search_fields = ['products']
    search_help_text = 'Поиск по полю продукта (products)'


# Register your models here.
admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)