from datetime import datetime

from django.core.management.base import BaseCommand
from myapp2.models import Order, Client

class Command(BaseCommand):
    help = "Update order by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        order = Order.objects.filter(pk=pk).first()
        order.date_ordered = datetime(2024, 3, 1)
        order.save()
        self.stdout.write(f'{order}')
