from django.core.management.base import BaseCommand
from myapp2.models import Order, Client

class Command(BaseCommand):
    help = "Update order by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')
        parser.add_argument('client', type=int, help='New Client ID')

    def handle(self, *args, **kwargs):
        client = Client.objects.get(pk=kwargs['client'])
        pk = kwargs.get('pk')
        order = Order.objects.filter(pk=pk).first()
        order.client = client
        order.save()
        self.stdout.write(f'{order}')
