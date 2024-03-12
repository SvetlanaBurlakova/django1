from django.db import models
from django.utils import timezone


# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=14)
    address = models.CharField(max_length=200)
    registration_date = models.DateField(default=timezone.now)


    def __str__(self):
        return (f'Clientname: {self.name}, email: {self.email}, phone:{self.phone}, address: {self.address}, '
                f'registration_date: {self}')


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField(default=0)
    date_added = models.DateField(default=timezone.now)


    def get_price(self):
        return self.price


    def __str__(self):
        return (f'Productname: {self.name}')


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'Order: Clientname={self.client.name}, products={self.products.all()} {self.total_price} {self.date_ordered}')

