from django.urls import path
from . import views, admin

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('coin/', views.coin, name='coin'),
    path('num/', views.num, name='num'),
]