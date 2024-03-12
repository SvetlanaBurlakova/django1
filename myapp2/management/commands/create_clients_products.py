import random

from django.core.management.base import BaseCommand
from myapp2.models import Client, Product


class Command(BaseCommand):
    help = "Generate fake clients and products."
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Client ID')
    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(name=f'Name{i}', email=f'mail{i}@mail.ru', phone=f'phone{i}', address=f'address{i}')
            client.save()
            product = Product(name=f'Product{i}', description=f'description{i}', price=random.uniform(10, 400),
                              count=random.randint(1, 10))
            product.save()


