from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'Home',
        'content': 'Головна сторінка магазина - SoftAndWood',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'bool': True,

    }

    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse('About page')
