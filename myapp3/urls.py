from django.urls import path
from . import views


urlpatterns = [
 path('', views.index, name='index'),
 path('about/', views.about, name='about'),
 path('user/<int:user_id>/posts', views.user_posts, name='user_posts'),
 path('user/<int:post_id>/', views.post, name='post'),
 path('authors/', views.authors, name='authors'),
]