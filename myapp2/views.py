from datetime import datetime, timedelta
from pytz import timezone
from django.http import HttpResponse
from django.shortcuts import render
from .models import Client, Order, Product
from .forms import ProductForm
from django.shortcuts import render, get_object_or_404
from django.core.files.storage import FileSystemStorage


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

    context = {'title': 'Неделя',
               'client': client,
               'products': goods}
    return render(request, 'myapp2/orders.html', context=context)

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

    context = {'title': 'месяц',
               'client': client,
               'products': goods}
    return render(request, 'myapp2/orders.html', context=context)


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

    context = {'title': 'Год',
               'client': client,
               'products': goods}
    return render(request, 'myapp2/orders.html', context=context)


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            Product(**form.cleaned_data).save()
    else:
        form = ProductForm()
    context = {
        'title': 'Добавление продукта',
        'form': form,
    }
    return render(request, 'myapp2/add_product.html', context=context)