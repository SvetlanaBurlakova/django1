from django.urls import path
from . import views


urlpatterns = [
 path('', views.index, name='index'),
 path('orders/<int:client_id>/week/', views.orders_week, name='orders_week'),
 path('orders/<int:client_id>/month/', views.orders_month, name='orders_month'),
 path('orders/<int:client_id>/year/', views.orders_year, name='orders_year'),
path('product/add', views.add_product, name='add_product'),
]