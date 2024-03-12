from django.core.management.base import BaseCommand
from myapp2.models import Order, Product


class Command(BaseCommand):
    help = "Get orders by Product id."
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')
    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        product = Product.objects.get(pk=pk)
        if product is not None:
            orders = Order.objects.filter(products=product)
        self.stdout.write(f'{orders}')

