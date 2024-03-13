from datetime import datetime, timedelta
from pytz import timezone
from django.http import HttpResponse
from django.shortcuts import render
from .models import Client, Order, Product
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    return HttpResponse("MAin")


def orders_week(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    goods = []
    if client:
        orders = Order.objects.filter(client=client).order_by('-date_ordered')

        for order in orders:
            date_order = order.date_ordered
            date_diff = datetime.now().replace(tzinfo=timezone('UTC')) - date_order
            if date_diff.days < 7:
                for product in order.products.all():
                    goods.append((product,date_order))

    context = {'title': 'Все заказы за Неделю',
               'client': client,
               'products': goods}
    return render(request, 'myapp2/orders_week.html', context=context)

def orders_month(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    goods = []
    if client:
        orders = Order.objects.filter(client=client).order_by('-date_ordered')

        for order in orders:
            date_order = order.date_ordered
            date_diff = datetime.now().replace(tzinfo=timezone('UTC')) - date_order
            if date_diff.days < 31:
                for product in order.products.all():
                    goods.append((product,date_order))

    context = {'title': 'Все заказы за месяц',
               'client': client,
               'products': goods}
    return render(request, 'myapp2/orders_week.html', context=context)


def orders_year(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    goods = []
    if client:
        orders = Order.objects.filter(client=client).order_by('-date_ordered')

        for order in orders:
            date_order = order.date_ordered
            date_diff = datetime.now().replace(tzinfo=timezone('UTC')) - date_order
            if date_diff.days < 365:
                for product in order.products.all():
                    goods.append((product,date_order))

    context = {'title': 'Все заказы за Год',
               'client': client,
               'products': goods}
    return render(request, 'myapp2/orders_week.html', context=context)
