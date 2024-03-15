import random
import logging
from django.shortcuts import render
from django.http import HttpResponse
from .models import CoinFlip
from .forms import ChoiceForm

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

def result(request):
    func = {"Coin": coin, "Hundred": num}
    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            count = form.cleaned_data['count']
            choice = form.cleaned_data['choice']
            return func[choice](request, count)
    else:
        form = ChoiceForm()
        message = 'Выберите действие и количество'
    return render(request, 'myapp4/user_form.html', {'form': form, 'message': message})