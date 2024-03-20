# # Register your models here.
# from django.contrib import admin
# from .models import Category, Product
#
# @admin.action(description="Сбросить количество в ноль")
# def reset_quantity(modeladmin, request, queryset):
#     queryset.update(quantity=0)
#
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['name', 'category', 'quantity']
#     ordering = ['category', '-quantity']
#     list_filter = ['date_added', 'price']
#     search_fields = ['description']
#     search_help_text = 'Поиск по полю Описание продукта (description)'
#
# # @admin.register(Author)
# # class AuthorAdmin(admin.ModelAdmin):
# #     list_display = ['name','email', 'birthdate']
# #     list_filter = ['name', 'birthdate']
# #     search_fields = ['name__startswith', 'email']
# #     readonly_fields = ['email']
# #     list_editable = ['birthdate']
#
#
# admin.site.register(Category)
# admin.site.register(Product, ProductAdmin)

