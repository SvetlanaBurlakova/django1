from django.urls import path
from . import views, admin

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]