from django.utils import timezone

from django.db import models
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import AbstractUser
# # Create your models here.
#
# class stUser1(AbstractUser):
#     username = models.CharField(max_length=100)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField()
#     biography = models.TextField()
#     password = models.CharField(max_length=100)


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(default='', blank=True)
    price = models.DecimalField(default=999999.99, max_digits=8, decimal_places=2)
    quantity = models.PositiveSmallIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(default=5.0, max_digits=3, decimal_places=2)

    @property
    def total_quantity(self):
        return sum(product.quantity for product in Product.objects.all())

# #author__name
#
# class User(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     password = models.CharField(max_length=100)
#     age = models.IntegerField()
#
#     def __str__(self):
#         return f'Username: {self.name}, email: {self.email}, age:{self.age}'

#
# StUser = get_user_model()
# # class Author(StUser):
# #     name = models.CharField(max_length=100)
# #     lastname = models.CharField(max_length=100)
# #     email = models.EmailField()
# #     biography = models.TextField()
# #     birthdate = models.DateField(default=timezone.now())
# #
# #     @property
# #     def fullname(self):
# #         return f'{self.name} {self.lastname}'
# #
# #
# #     def __str__(self):
# #         return f'Name: {self.name}, email: {self.email}'
#
#
# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     date_publication = models.DateField(auto_now_add=True)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     is_published = models.BooleanField()
#     views = models.IntegerField(default=0)
#
#     def __str__(self):
#         return f'Title is {self.title}'
#
