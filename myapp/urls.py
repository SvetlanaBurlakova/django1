from django.urls import path
from . import views, admin

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('coin/<int:amount_flips>/', views.coin, name='coin'),
    path('num/<int:amount_flips>/', views.num, name='num'),
]