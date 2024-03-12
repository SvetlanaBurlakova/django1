from django.core.management.base import BaseCommand
from myapp2.models import Client, Product, Order

class Command(BaseCommand):
    help = "Create order."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='ClientID')
        parser.add_argument('products', type=str, help='products')

    def handle(self, *args, **kwargs):
        client = Client.objects.get(pk=kwargs['pk'])
        products_id = kwargs['products'].split(',')
        products_ids = [int(id) for id in products_id]
        products = Product.objects.filter(id__in=products_ids)
        total_price = sum([product.get_price() for product in products])
        order = Order(client=client, total_price=total_price)
        order.save()
        order.products.set(products)
        self.stdout.write(f'{order}')
