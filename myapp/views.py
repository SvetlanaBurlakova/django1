import random
import logging
from django.shortcuts import render
from django.http import HttpResponse
from .models import CoinFlip

# Create your views here.

logger = logging.getLogger(__name__)


def index(request):
    logger.debug(request)
    return render(request, 'myapp/index.html', context = {'title':'Главная страница'})


def about(request):
    logger.debug(request)
    return render(request, 'myapp/about.html', context = {'title':'О нас'})


def coin(request, amount_flips):
    coins = ['head', 'tail']
    coin = random.choice(coins)
    logger.debug(coin)
    result = [random.choice(coins) for _ in range(amount_flips)]
    #CoinFlip(side=coin).save()
    context = {'title': 'Бросание монеты',
              'last_result': result}
    return render(request, 'myapp/coin.html', context=context)


def num(request, amount_flips):
    #num = random.randint(num)
    logger.debug(num)
    result = [random.randint(1,7) for _ in range(amount_flips)]
    context = {'title': 'Бросание монеты',
              'last_result': result}
    return render(request, 'myapp/num.html', context=context)


