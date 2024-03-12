import random
import logging
from django.shortcuts import render
from django.http import HttpResponse
from .models import CoinFlip

# Create your views here.

logger = logging.getLogger(__name__)


def index(request):
    logger.debug(request)
    return render(request, 'index.html')


def about(request):
    logger.debug(request)
    return HttpResponse("About us")


def coin(request):
    coins = ['head', 'tail']
    coin = random.choice(coins)
    logger.debug(coin)
    CoinFlip(side=coin).save()
    context = {'current': coin,
              'last_result': CoinFlip.get_last_fields(3)}
    return render(request, 'coin.html', context)


def num(request):
    num = random.randint(num)
    logger.debug(num)
    return HttpResponse(f'Выпал {num}')

def about(request):
    logger.debug(request)
    return HttpResponse("About us")


