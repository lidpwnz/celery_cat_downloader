from django.shortcuts import render
from django.http import HttpResponse
from .tasks import download_a_cat, test_func


def home(request):
    print('1')
    download_a_cat.delay()
    return HttpResponse('<h1>Hello World!!</h1>')


def test(request):
    test_func.delay()
    return HttpResponse('Done')
