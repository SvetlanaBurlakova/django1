import random
import logging
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

logger = logging.getLogger(__name__)


def index(request):
    logger.debug(request)
    return render(request, 'index.html')


def about(request):
    logger.debug(request)
    return HttpResponse("About us")


